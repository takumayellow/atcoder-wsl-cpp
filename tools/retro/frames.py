"""録画から一定間隔でコマを抜き、実時刻のラベルをつけた一覧画像（コンタクトシート）にする。

一覧画像は Claude が Read で読んで「その時刻に画面で何をしていたか」を拾うためのもの。
コードの中身は actest のスナップショット（.snap/）のほうが確かなので、ここでは
画面の切り替わり（エディタ・ブラウザ・解説・Claude とのやりとり）を追うのに使う。

    py -3.13 tools/retro/frames.py "C:/Users/takum/Videos/2026-09-30 23-16-00.mp4" --out <作業ディレクトリ> --every 30
    py -3.13 tools/retro/frames.py <録画> --out <dir> --from 23:40 --to 23:50 --every 5   # 気になる区間を細かく

出力: <out>/<録画名>/sheet_000.jpg ...（1 枚に cols×rows コマ）
"""
from __future__ import annotations

import argparse
import datetime as dt
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from rectime import base_time, clock_offset

FONT_CANDIDATES = ("C:/Windows/Fonts/meiryo.ttc", "C:/Windows/Fonts/msgothic.ttc",
                   "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")


def load_font(size: int) -> ImageFont.FreeTypeFont:
    for path in FONT_CANDIDATES:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default(size)


def duration(video: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(video)],
        capture_output=True, text=True, check=True,
    ).stdout
    return float(out.strip())


def grab(video: Path, lo: float, hi: float, every: float, width: int, dst: Path) -> list[tuple[float, Path]]:
    """lo〜hi 秒を every 秒おきに抜く。返り値は（録画開始からの秒, 画像）の並び。"""
    subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-ss", str(lo), "-t", str(hi - lo), "-i", str(video),
         "-vf", f"fps=1/{every},scale={width}:-2", "-q:v", "4", str(dst / "f_%05d.jpg")],
        check=True,
    )
    frames = sorted(dst.glob("f_*.jpg"))
    return [(lo + i * every, f) for i, f in enumerate(frames)]


def make_sheets(frames, start_at: dt.datetime, cols: int, rows: int, out_dir: Path) -> list[Path]:
    if not frames:
        return []
    w, h = Image.open(frames[0][1]).size
    font = load_font(max(14, w // 18))
    label_h = font.size + 8
    per = cols * rows
    written = []
    for n in range(0, len(frames), per):
        page = frames[n:n + per]
        sheet = Image.new("RGB", (cols * w, rows * (h + label_h)), "white")
        draw = ImageDraw.Draw(sheet)
        for i, (sec, path) in enumerate(page):
            x, y = (i % cols) * w, (i // cols) * (h + label_h)
            draw.text((x + 6, y + 3), f"{start_at + dt.timedelta(seconds=sec):%H:%M:%S}", fill="black", font=font)
            sheet.paste(Image.open(path), (x, y + label_h))
        dst = out_dir / f"sheet_{n // per:03d}.jpg"
        sheet.save(dst, quality=85)
        written.append(dst)
    return written


def main() -> None:
    p = argparse.ArgumentParser(description="録画のコマを時刻ラベルつきの一覧画像にする")
    p.add_argument("video", type=Path)
    p.add_argument("--out", type=Path, required=True, help="出力先（リポジトリの外。scratchpad など）")
    p.add_argument("--every", type=float, default=30, help="何秒おきに抜くか")
    p.add_argument("--from", dest="from_", metavar="HH:MM", help="この時刻から（録画の実時刻）")
    p.add_argument("--to", metavar="HH:MM", help="この時刻まで（録画の実時刻）")
    p.add_argument("--cols", type=int, default=4)
    p.add_argument("--rows", type=int, default=3)
    p.add_argument("--width", type=int, default=640, help="1 コマの幅（px）。コードを読みたいときは広げる")
    p.add_argument("--base", help="録画の開始時刻（ISO 形式）。ファイル名から読めないときに使う")
    args = p.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", newline="\n")
    sys.stderr.reconfigure(encoding="utf-8", newline="\n")

    start_at = base_time(args.video, args.base)
    total = duration(args.video)
    lo = clock_offset(args.from_, start_at, 0.0)
    hi = min(total, clock_offset(args.to, start_at, total))
    if hi <= lo:
        sys.exit("--from が --to より後、または録画の範囲外です")
    out_dir = args.out / args.video.stem
    out_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        frames = grab(args.video, lo, hi, args.every, args.width, Path(tmp))
        sheets = make_sheets(frames, start_at, args.cols, args.rows, out_dir)
    print(f"{len(frames)} コマ → {len(sheets)} 枚: {out_dir}")


if __name__ == "__main__":
    main()
