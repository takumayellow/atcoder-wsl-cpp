"""解いている間に Claude と交わした会話を、時刻つきで抜き出す。

画面録画からチャット欄を読むより、Claude Code の会話ログ（~/.claude*/projects/*/*.jsonl）を
直接読むほうが正確。ログの時刻は UTC なので日本時間に直して出す。

    py -3.13 tools/retro/claude_log.py --since "2026-09-30 19:00" --until "2026-10-01 00:00" --cwd atcoder-wsl-cpp
    py -3.13 tools/retro/claude_log.py --since "2026-09-30 19:00" --until "2026-09-30 23:00" --cwd icpc-team-2026

出力は 1 行 1 発言の TSV（時刻 / user か assistant / 本文）。--max-chars で本文を切り詰める。
ツールの呼び出しと結果は出さない（--tools で道具の名前だけ出す）。
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

JST = dt.timezone(dt.timedelta(hours=9))
TAGGED = re.compile(r"<(system-reminder|command-[a-z-]+|local-command-[a-z-]+)>.*?</\1>", re.S)


def local_time(s: str) -> dt.datetime:
    t = dt.datetime.fromisoformat(s)
    return t.replace(tzinfo=JST) if t.tzinfo is None else t.astimezone(JST)


def log_files(roots: list[Path]) -> list[Path]:
    return sorted(f for root in roots for f in root.glob("projects/*/*.jsonl"))


def texts(entry: dict, with_tools: bool) -> str:
    content = (entry.get("message") or {}).get("content")
    if isinstance(content, str):
        parts = [content]
    elif isinstance(content, list):
        parts = []
        for block in content:
            kind = block.get("type")
            if kind == "text":
                parts.append(block.get("text", ""))
            elif kind == "tool_use" and with_tools:
                parts.append(f"[{block.get('name')}]")
    else:
        return ""
    return " ".join(TAGGED.sub("", p).strip() for p in parts if p).strip()


def collect(files, since, until, cwd, with_tools):
    # アカウントごとの ~/.claude* が projects を共有（ジャンクション）していると、同じ会話が
    # 何度も見つかる。発言ごとの uuid で 1 回だけ数える
    rows, seen = [], set()
    for f in files:
        with f.open(encoding="utf-8") as fh:
            for line in fh:
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if entry.get("type") not in ("user", "assistant") or "timestamp" not in entry:
                    continue
                if entry.get("isMeta") or entry.get("isCompactSummary") or entry.get("isSidechain"):
                    continue
                at = local_time(entry["timestamp"])
                if not since <= at < until:
                    continue
                if cwd and cwd not in (entry.get("cwd") or ""):
                    continue
                uid = entry.get("uuid")
                if uid:
                    if uid in seen:
                        continue
                    seen.add(uid)
                body = texts(entry, with_tools)
                if body:
                    rows.append((at, entry["type"], body))
    return sorted(rows)


def main() -> None:
    p = argparse.ArgumentParser(description="Claude Code の会話を時間帯で抜き出す")
    p.add_argument("--since", required=True, help='日本時間。例 "2026-09-30 19:00"')
    p.add_argument("--until", required=True, help='日本時間。例 "2026-10-01 00:00"')
    # ~/.claude* には仕事のアカウントの会話も入っているので、解いたリポジトリの会話だけに絞る
    p.add_argument("--cwd", required=True, help="作業ディレクトリにこの文字列を含む会話だけ（例 atcoder-wsl-cpp）")
    p.add_argument("--max-chars", type=int, default=400, help="1 発言の最大文字数（0 で切らない）")
    p.add_argument("--tools", action="store_true", help="ツール呼び出しを [Bash] のように名前だけ出す")
    p.add_argument("--root", type=Path, action="append",
                   help="ログの置き場（既定は ~/.claude* 全部。アカウントを分けている場合に効く）")
    args = p.parse_args()

    roots = args.root or sorted(Path.home().glob(".claude*"))
    since, until = local_time(args.since), local_time(args.until)
    rows = collect(log_files(roots), since, until, args.cwd, args.tools)
    out = sys.stdout
    out.reconfigure(encoding="utf-8", newline="\n")
    sys.stderr.reconfigure(encoding="utf-8", newline="\n")
    for at, role, body in rows:
        body = " ".join(body.split())
        if args.max_chars and len(body) > args.max_chars:
            body = body[:args.max_chars] + "…"
        out.write(f"{at:%m-%d %H:%M:%S}\t{role}\t{body}\n")


if __name__ == "__main__":
    main()
