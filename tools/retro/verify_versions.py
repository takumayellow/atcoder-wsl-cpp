"""途中の版（actest のスナップショットなど）を、愚直解と小さい入力の全通り・ランダムで突き合わせる。

振り返りで「この版はどの入力で何件落ちるか」「最初の反例は何か」を数字で出すために使う。

    python3 tools/retro/verify_versions.py --gen gen.py <問題ディレクトリ>/.snap/*.py main.py

gen.py には次を書く:
    def cases():          # 入力文字列（1 回の実行に渡す標準入力）を順に返す
        ...
    def solve(inp: str):  # 正解の出力を返す（愚直解）。--brute brute.py で別プログラムにしてもよい
        ...

Python の版は同じプロセスの中で exec して速く回す（数万件でも数秒）。
open(0) を使う版・C++ の版・無限ループしうる版は 1 件ごとに別プロセスで動かす
（--isolate で Python の版も別プロセスにできる。--timeout 秒で打ち切る）。
別プロセスは 1 件 20ms ほどかかるので、件数が多いときは --limit で絞る。
出力は空白区切りの語の並びとして比べる。
"""
from __future__ import annotations

import argparse
import contextlib
import importlib.util
import io
import itertools
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def load_gen(path: Path):
    spec = importlib.util.spec_from_file_location("retro_gen", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "cases"):
        sys.exit(f"{path}: cases() がありません")
    return mod


class InProcess:
    """Python の版を exec で動かす。sys.stdin / sys.stdout を差し替える。"""

    def __init__(self, path: Path):
        self.code = compile(path.read_text(encoding="utf-8"), str(path), "exec")

    def __call__(self, inp: str) -> str:
        out = io.StringIO()
        saved = sys.stdin
        sys.stdin = io.TextIOWrapper(io.BytesIO(inp.encode()), encoding="utf-8")
        try:
            with contextlib.redirect_stdout(out):
                exec(self.code, {"__name__": "__main__"})
        except SystemExit:
            pass
        except Exception as e:  # 実行時エラーも「その版の出力」として数える
            return f"<{type(e).__name__}: {e}>"
        finally:
            sys.stdin = saved
        return out.getvalue()


class Subprocess:
    def __init__(self, cmd: list[str], timeout: float):
        self.cmd, self.timeout = cmd, timeout

    def __call__(self, inp: str) -> str:
        try:
            r = subprocess.run(self.cmd, input=inp, capture_output=True, text=True, timeout=self.timeout)
        except subprocess.TimeoutExpired:
            return "<TLE>"
        return r.stdout if r.returncode == 0 else r.stdout + f"<exit {r.returncode}>"


def runner(path: Path, isolate: bool, timeout: float, build_dir: Path):
    if path.suffix == ".py":
        src = path.read_text(encoding="utf-8")
        if isolate or "open(0)" in src:
            return Subprocess([sys.executable, str(path)], timeout)
        return InProcess(path)
    if path.suffix == ".cpp":
        if not shutil.which("g++"):
            sys.exit("C++ の版を試すには g++ が要ります（WSL の python3 で動かす）")
        exe = build_dir / f"{path.stem}_{abs(hash(str(path)))}.out"
        r = subprocess.run(["g++", "-std=c++17", "-O2", "-o", str(exe), str(path)], capture_output=True, text=True)
        if r.returncode != 0:
            return None
        return Subprocess([str(exe)], timeout)
    sys.exit(f"{path}: .py と .cpp だけ扱える")


def reference(gen, brute: Path | None, timeout: float, build_dir: Path):
    if brute:
        return runner(brute, False, timeout, build_dir)
    if hasattr(gen, "solve"):
        return lambda inp: str(gen.solve(inp))
    sys.exit("正解の出し方がありません。gen.py に solve() を書くか --brute を渡してください")


def show(inp: str) -> str:
    one = inp.strip().replace("\n", " / ")
    return one if len(one) <= 80 else one[:80] + "…"


def main() -> None:
    p = argparse.ArgumentParser(description="途中の版を愚直解と突き合わせる")
    p.add_argument("versions", nargs="+", type=Path)
    p.add_argument("--gen", type=Path, required=True, help="cases()（と solve()）を書いたファイル")
    p.add_argument("--brute", type=Path, help="愚直解のプログラム（gen.py の solve() の代わり）")
    p.add_argument("--limit", type=int, help="先頭からこの件数だけ試す")
    p.add_argument("--isolate", action="store_true", help="Python の版も 1 件ずつ別プロセスで動かす")
    p.add_argument("--timeout", type=float, default=2.0, help="別プロセスで動かすときの 1 件あたりの秒数")
    args = p.parse_args()

    sys.stdout.reconfigure(encoding="utf-8", newline="\n")
    sys.stderr.reconfigure(encoding="utf-8", newline="\n")
    gen = load_gen(args.gen)
    cases = list(itertools.islice(gen.cases(), args.limit))
    with tempfile.TemporaryDirectory() as tmp:
        build_dir = Path(tmp)
        ref = reference(gen, args.brute, args.timeout, build_dir)
        want = [ref(c).split() for c in cases]
        print(f"{len(cases)} 件で比較")
        for path in args.versions:
            run = runner(path, args.isolate, args.timeout, build_dir)
            if run is None:
                print(f"{path}\tコンパイルエラー")
                continue
            bad = []
            for i, (c, w) in enumerate(zip(cases, want), 1):
                if (g := run(c).split()) != w:
                    bad.append((c, w, g))
                if isinstance(run, Subprocess) and i % 500 == 0:
                    print(f"  {path}: {i} / {len(cases)}", file=sys.stderr, flush=True)
            line = f"{path}\t不一致 {len(bad)} / {len(cases)}"
            if bad:
                c, w, g = bad[0]
                line += f"\t最初の反例: {show(c)} → 正解 {' '.join(w)} / この版 {' '.join(g)[:60]}"
            print(line, flush=True)


if __name__ == "__main__":
    main()
