"""録画から独り言を文字起こしし、録画の実時刻をつけて TSV に書く。

Windows 側の Python で動かす（WSL ではない）:
    py -3.13 tools/retro/transcribe_rec.py "C:/Users/takum/Videos/2026-09-30 19-21-27.mp4" --out <作業ディレクトリ>

処理の順:
  1. ffmpeg で音声を 10 分ずつ 16 kHz モノラルに切り出す（--track で音声トラック、--from/--to で範囲を選ぶ）
  2. --separate のときは声だけを分離する（マイクと PC の音が同じトラックに混ざっている録画用）
  3. VAD（faster-whisper の発話区間検出）で発話だけを切り出す
  4. 1 区間ずつ Groq Whisper に送る。プロンプトは付けない
     （つないだ音声をまとめて送ると時刻がずれ、プロンプトを付けると無音区間にプロンプトの文が出てくる）

出力 <out>/<録画名>.tsv は 1 行 1 発話で「時刻 / 秒数 / no_speech_prob / 本文」。
途中で止めても、もう一度同じコマンドを打てば済んだ区間は飛ばして続きから送る。

GROQ_API_KEY は tus-tools/.env から読む（RETRO_ENV_FILE で変えられる）。キーは表示しない。
"""
from __future__ import annotations

import argparse
import datetime as dt
import io
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import numpy as np
import soundfile as sf

from rectime import base_time, clock_offset

SR = 16000
CHUNK_SEC = 600
ENV_FILE = Path(os.environ.get("RETRO_ENV_FILE", Path.home() / "dev/tus-tools/.env"))
SEPARATOR = Path(os.environ.get("RETRO_SEPARATOR", Path.home() / "dev/voice-lab/.venv/Scripts/audio-separator.exe"))
SEPARATOR_MODELS = Path(os.environ.get("RETRO_SEPARATOR_MODELS", Path.home() / "dev/voice-lab/models/audio_separator"))
SEPARATOR_MODEL = "UVR-MDX-NET-Voc_FT.onnx"
# 小さいマイク入力を持ち上げる。highpass で空調などの低音を落としてから音量をならす
AUDIO_FILTER = "highpass=f=80,dynaudnorm=f=250:g=15:m=100:p=0.9"
# Whisper が無音や雑音から作りがちな定型文。no_speech_prob が高いときだけ捨てる
HALLUCINATIONS = ("ご視聴ありがとうございました", "チャンネル登録", "おやすみなさい", "字幕")


def duration(video: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(video)],
        capture_output=True, text=True, check=True,
    ).stdout
    return float(out.strip())


def extract_chunk(video: Path, track: int, start: float, length: float, dst: Path) -> None:
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-ss", str(start), "-t", str(length), "-i", str(video),
         "-map", f"0:a:{track}", "-ac", "1", "-ar", str(SR), str(dst)],
        check=True,
    )


def separate_vocals(src: Path, workdir: Path) -> Path:
    if not SEPARATOR.exists():
        sys.exit(f"声の分離ツールがありません: {SEPARATOR}（RETRO_SEPARATOR で場所を指定するか、--separate を外す）")
    subprocess.run(
        [str(SEPARATOR), str(src), "--model_filename", SEPARATOR_MODEL, "--model_file_dir", str(SEPARATOR_MODELS),
         "--output_dir", str(workdir), "--single_stem", "Vocals", "--output_format", "WAV"],
        check=True, capture_output=True,
    )
    found = sorted(workdir.glob(f"{src.stem}_(Vocals)*.wav"))
    if not found:
        sys.exit(f"{src.name}: 分離後の音声が見つかりません")
    return found[0]


def load_normalized(path: Path) -> np.ndarray:
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(path), "-af", AUDIO_FILTER, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
        capture_output=True, check=True,
    ).stdout
    return np.frombuffer(raw, dtype=np.float32)


def speech_spans(audio: np.ndarray, threshold: float) -> list[tuple[int, int]]:
    from faster_whisper.vad import VadOptions, get_speech_timestamps

    opts = VadOptions(threshold=threshold, min_silence_duration_ms=600, speech_pad_ms=300, min_speech_duration_ms=250)
    return [(t["start"], t["end"]) for t in get_speech_timestamps(audio, opts)]


def groq_client():
    from dotenv import dotenv_values
    from openai import OpenAI

    # .env には他のキーもあるので GROQ_API_KEY だけを読む（ffmpeg などの子プロセスの環境に載せない）
    key = os.environ.get("GROQ_API_KEY") or dotenv_values(ENV_FILE).get("GROQ_API_KEY")
    if not key:
        sys.exit(f"GROQ_API_KEY がありません（{ENV_FILE} を確認）")
    return OpenAI(api_key=key, base_url="https://api.groq.com/openai/v1")


def transcribe_clip(client, clip: np.ndarray, model: str) -> tuple[str, float]:
    from openai import RateLimitError

    buf = io.BytesIO()
    sf.write(buf, clip, SR, format="FLAC")
    while True:
        buf.seek(0)
        buf.name = "clip.flac"
        try:
            r = client.audio.transcriptions.create(
                model=model, file=buf, language="ja", response_format="verbose_json", temperature=0,
            )
            break
        except RateLimitError as e:
            wait = int(float(e.response.headers.get("retry-after", 30))) + 3
            print(f"  Groq の回数制限。{wait} 秒待つ", flush=True)
            time.sleep(wait)
    segs = [s if isinstance(s, dict) else s.model_dump() for s in (r.segments or [])]
    text = " ".join(s["text"].strip() for s in segs).strip()
    no_speech = min((s["no_speech_prob"] for s in segs), default=1.0)
    return text, no_speech


def done_spans(out: Path) -> set[tuple[str, str]]:
    """書き終えた区間の（時刻, 秒数）。同じ秒に始まる区間が 2 つあっても区別できるよう秒数も使う。"""
    if not out.exists():
        return set()
    return {tuple(line.split("\t", 2)[:2]) for line in out.read_text(encoding="utf-8").splitlines() if line}


def is_noise(text: str, no_speech: float) -> bool:
    return not text or (no_speech > 0.6 and any(h in text for h in HALLUCINATIONS))


def process(video: Path, args, client) -> Path:
    start_at = base_time(video, args.base)
    out = args.out / f"{video.stem}.tsv"
    seen = done_spans(out)
    total = duration(video)
    lo = int(clock_offset(args.from_, start_at, 0.0))
    hi = min(total, clock_offset(args.to, start_at, total))
    print(f"{video.name}: {total / 60:.0f} 分、開始 {start_at:%H:%M:%S}", flush=True)
    with tempfile.TemporaryDirectory() as tmp, out.open("a", encoding="utf-8", newline="\n") as fh:
        tmpdir = Path(tmp)
        for idx, chunk_start in enumerate(range(lo, int(hi), CHUNK_SEC)):
            wav = tmpdir / f"c{idx:03d}.wav"
            extract_chunk(video, args.track, chunk_start, min(CHUNK_SEC, hi - chunk_start), wav)
            src = separate_vocals(wav, tmpdir) if args.separate else wav
            audio = load_normalized(src)
            spans = speech_spans(audio, args.vad_threshold)
            kept = 0
            for s, e in spans:
                at = start_at + dt.timedelta(seconds=chunk_start + s / SR)
                key = (at.strftime("%H:%M:%S"), f"{(e - s) / SR:.1f}")
                if key in seen:
                    continue
                seen.add(key)
                text, no_speech = transcribe_clip(client, audio[s:e], args.model)
                if is_noise(text, no_speech):
                    continue
                fh.write(f"{key[0]}\t{key[1]}\t{no_speech:.2f}\t{text}\n")
                fh.flush()
                kept += 1
            at = start_at + dt.timedelta(seconds=chunk_start)
            print(f"  {at:%H:%M}〜: 発話 {len(spans)} 区間、書いた {kept} 行", flush=True)
    return out


def main() -> None:
    p = argparse.ArgumentParser(description="録画の独り言を時刻つきで文字起こしする")
    p.add_argument("videos", nargs="+", type=Path)
    p.add_argument("--out", type=Path, required=True, help="TSV を書くディレクトリ（リポジトリの外。scratchpad など）")
    p.add_argument("--track", type=int, default=0, help="使う音声トラック（0 始まり）。マイクだけのトラックがあればそれを選ぶ")
    p.add_argument("--separate", action="store_true", help="マイクと PC の音が混ざっているときに声だけを分離する")
    p.add_argument("--vad-threshold", type=float, default=0.4, help="発話とみなす閾値。拾い漏れが多ければ下げる")
    p.add_argument("--from", dest="from_", metavar="HH:MM", help="この時刻から（録画の実時刻）")
    p.add_argument("--to", metavar="HH:MM", help="この時刻まで（録画の実時刻）")
    p.add_argument("--base", help="録画の開始時刻（ISO 形式）。ファイル名から読めないときに使う")
    p.add_argument("--model", default=os.environ.get("GROQ_WHISPER_MODEL", "whisper-large-v3"))
    args = p.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", newline="\n")
    sys.stderr.reconfigure(encoding="utf-8", newline="\n")
    args.out.mkdir(parents=True, exist_ok=True)
    client = groq_client()
    for video in args.videos:
        print(f"-> {process(video, args, client)}", flush=True)


if __name__ == "__main__":
    main()
