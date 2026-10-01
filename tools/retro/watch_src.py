"""解いている間、ソースが保存されるたびに .snap/ へ写す（エディタや実行方法に依らない）。

録画を始めるときに、tmux の別ウィンドウなどで起動しておく。Ctrl+C で止まる:
    python3 tools/retro/watch_src.py ~/dev/icpc-team-2026/contest/2026/JAG/c
    python3 tools/retro/watch_src.py abc477            # コンテストのフォルダごと見張る

写し先は各ファイルと同じフォルダの .snap/<日時>_save-<ファイル名>（例 .snap/20260930-194512_save-main.py）。
actest の .snap/<日時>_<ok|ng|ce>.<拡張子> と同じ場所に並ぶので、solve-retro はどちらも同じように読める。
中身が前回と同じなら写さない。保存が続いている間は待ち、--settle 秒止まってから写す。
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import shutil
import sys
import time
from pathlib import Path

SKIP_DIRS = {".snap", "history", ".git", "node_modules", "bin", "obj", "__pycache__", "test"}


def sources(root: Path, exts: set[str]):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for name in filenames:
            if Path(name).suffix.lstrip(".") in exts:
                yield Path(dirpath) / name


def latest_snapshot(path: Path) -> bytes | None:
    """前回の見張りで最後に写した中身（起動し直したときに同じ版を重ねて写さないため）。"""
    found = sorted((path.parent / ".snap").glob(f"*_save-{path.name}"))
    try:
        return found[-1].read_bytes() if found else None
    except OSError:
        return None


def snapshot(path: Path, body: bytes) -> Path:
    """読んだ中身をそのまま書く（読んでから写すまでの間にエディタが書き換えても、読んだ版が残る）。"""
    snap = path.parent / ".snap"
    snap.mkdir(exist_ok=True)
    stamp = f"{dt.datetime.now():%Y%m%d-%H%M%S}"
    dst = snap / f"{stamp}_save-{path.name}"
    n = 1
    while dst.exists():  # 同じ秒に 2 版目が来たら -2, -3 … をつけて上書きしない
        n += 1
        dst = snap / f"{stamp}-{n}_save-{path.name}"
    dst.write_bytes(body)
    shutil.copystat(path, dst)
    return dst


def main() -> None:
    p = argparse.ArgumentParser(description="保存のたびにソースを .snap/ へ写す")
    p.add_argument("roots", nargs="*", type=Path, default=[Path(".")], help="見張るフォルダ（既定は今いる所）")
    p.add_argument("--ext", nargs="+", default=["py", "cpp", "cs"], help="対象の拡張子")
    p.add_argument("--interval", type=float, default=1.0, help="何秒おきに見るか")
    p.add_argument("--settle", type=float, default=2.0, help="最後の変更からこの秒数たってから写す")
    args = p.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", newline="\n")

    exts = set(args.ext)
    saved: dict[Path, bytes] = {}                  # 最後に写した中身
    changed: dict[Path, tuple[bytes, float]] = {}  # まだ写していない中身と、それを最初に見た時刻
    roots = [r.resolve() for r in args.roots]
    print(f"見張り開始: {', '.join(map(str, roots))}（Ctrl+C で止まる）", flush=True)
    first = True
    try:
        while True:
            now = time.monotonic()
            for path in (f for r in roots for f in sources(r, exts)):
                try:
                    body = path.read_bytes()
                except OSError:
                    continue
                if path not in saved:
                    saved[path] = latest_snapshot(path)
                if saved[path] == body:
                    changed.pop(path, None)
                    continue
                if path not in changed or changed[path][0] != body:
                    # 起動した時点の中身はすぐ 1 版として残す。以後は変更が止まるのを待つ
                    changed[path] = (body, now - args.settle if first else now)
                if now - changed[path][1] >= args.settle:
                    try:
                        dst = snapshot(path, body)
                    except OSError as e:  # .snap がファイルになっている・書けないなど。見張りは続ける
                        print(f"{path}: 控えを書けない（{e}）", file=sys.stderr, flush=True)
                        saved[path] = body  # 同じ版で毎回警告しない。次に中身が変わったらまた試す
                        del changed[path]
                        continue
                    saved[path] = body
                    del changed[path]
                    print(f"{dt.datetime.now():%H:%M:%S}  {path.parent.name}/{path.name} → .snap/{dst.name}", flush=True)
            first = False
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("見張り終了", flush=True)


if __name__ == "__main__":
    main()
