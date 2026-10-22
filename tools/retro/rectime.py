"""録画ファイル名と時計の時刻を扱う小さな共通部品（tools/retro の各スクリプトが import する）。"""
from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

OBS_NAME = re.compile(r"(\d{4}-\d{2}-\d{2})[ _](\d{2})-(\d{2})-(\d{2})")


def base_time(video: Path, override: str | None = None) -> dt.datetime:
    """録画の開始時刻。OBS の既定のファイル名（2026-09-30 19-21-27.mp4）から読む。"""
    if override:
        return dt.datetime.fromisoformat(override)
    m = OBS_NAME.search(video.name)
    if not m:
        sys.exit(f"{video.name}: ファイル名から開始時刻を読めません。--base 2026-09-30T19:21:27 で指定してください")
    return dt.datetime.fromisoformat(f"{m.group(1)}T{m.group(2)}:{m.group(3)}:{m.group(4)}")


def clock_offset(clock: str | None, start: dt.datetime, default: float) -> float:
    """「23:40」「23:40:30」を録画開始からの秒数にする。開始より前の時刻は翌日として扱う。
    clock が無ければ default を返す。"""
    if clock is None:
        return default
    parts = [int(p) for p in clock.split(":")]
    if len(parts) not in (2, 3):
        sys.exit(f"{clock}: 時刻は HH:MM か HH:MM:SS で書いてください")
    h, m, s = (parts + [0])[:3]
    at = start.replace(hour=h, minute=m, second=s)
    if at < start:
        at += dt.timedelta(days=1)
    return (at - start).total_seconds()
