"""vim の undo の履歴から、変更ごとの版を時刻つきで取り出す（保存しなかった途中の変更も含む）。

vim を undofile つきで使っていれば、解く前の準備は要らない（dotfiles の _vimrc で ~/.vim/undo に残している）。
編集したのと同じ環境で動かす（WSL の vim で書いたなら WSL の python3。履歴はファイルのフルパスで引くため）:
    python3 tools/retro/undo_versions.py main.py --out <作業ディレクトリ>
    python3 tools/retro/undo_versions.py main.py --out <dir> --from 23:40 --to 23:50   # 区間だけ

出力 <out>/<ファイル名>/:
  changes.txt                          変更ごとの「時刻・番号・保存したか・差分」。独り言の TSV と時刻で突き合わせる
  <日時>_u<番号>[_s<保存番号>].<拡張子>  その変更の直後の中身（verify_versions.py にそのまま渡せる）

履歴が残らないのは、最後の保存のあとで :q! した変更と、vim の外（Claude の Edit など）で書き換えたファイル
（中身が履歴と合わなくなり、vim が履歴を読まない）。古い変更は undolevels（既定 1000）を超えると消える。
"""
from __future__ import annotations

import argparse
import datetime as dt
import difflib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# 履歴の木（undo してから別の変更をした枝も含む）を番号順にたどり、各変更の直後の中身を書き出す。
# 枝の差分を正しく出すため、各変更がどの状態の上に加えられたか（親の番号）も残す
VIM_SCRIPT = r"""
function! s:walk(entries, parent, acc) abort
  let prev = a:parent
  for e in a:entries
    call add(a:acc, [e, prev])
    if has_key(e, 'alt')
      call s:walk(e.alt, prev, a:acc)
    endif
    let prev = e.seq
  endfor
endfunction
let s:all = []
call s:walk(undotree().entries, 0, s:all)
let s:meta = []
for [s:e, s:parent] in sort(s:all, {a, b -> a[0].seq - b[0].seq})
  execute 'silent undo ' . s:e.seq
  call writefile(getline(1, '$'), g:retro_out . '/' . s:e.seq . '.txt')
  call add(s:meta, s:e.seq . "\t" . s:parent . "\t" . s:e.time . "\t" . get(s:e, 'save', ''))
endfor
silent undo 0
call writefile(getline(1, '$'), g:retro_out . '/0.txt')
call writefile(s:meta, g:retro_out . '/meta.tsv')
qa!
"""


def dump_history(src: Path, undodir: Path, work: Path) -> list[tuple[int, int, dt.datetime, str]]:
    def lit(path: Path) -> str:  # vim の '...' 文字列にする
        return "'" + str(path).replace("'", "''") + "'"

    script = work / "dump.vim"
    script.write_text(VIM_SCRIPT, encoding="utf-8")
    # 利用者の vimrc は読まず、undo の設定だけ入れる（ファイルを読む前に効かせるため --cmd で渡す）
    subprocess.run(
        ["vim", "-u", "NONE", "-N", "-es", "-n",
         "--cmd", "set undofile", "--cmd", f"let &undodir = {lit(undodir)}",
         "--cmd", f"let g:retro_out = {lit(work)}", "-S", str(script), str(src)],
        check=False, stdin=subprocess.DEVNULL,
    )
    meta = work / "meta.tsv"
    if not meta.exists():
        sys.exit(f"{src}: 履歴を読めませんでした（vim が途中で止まった）")
    rows = []
    for line in meta.read_text(encoding="utf-8").splitlines():
        seq, parent, t, save = line.split("\t")
        rows.append((int(seq), int(parent), dt.datetime.fromtimestamp(int(t)), save))
    return rows


def clock_match(when: dt.datetime, clock: str | None, after: bool) -> bool:
    if clock is None:
        return True
    h, m, *s = (int(p) for p in clock.split(":"))
    t = dt.time(h, m, s[0] if s else 0)
    return when.time() >= t if after else when.time() <= t


def describe(old: list[str], new: list[str]) -> list[str]:
    """差分を「@@ 行番号」と +/- の行で表す（前後の文脈は付けない）。"""
    out = []
    for line in difflib.unified_diff(old, new, n=0, lineterm=""):
        if line.startswith(("---", "+++")):
            continue
        if line.startswith("@@"):
            old, new = (part.lstrip("-+").split(",") for part in line.split()[1:3])
            start = old[0] if new[1:] == ["0"] else new[0]  # 削除だけの塊は、消えた行の元の位置
            out.append(f"  @@ {start} 行目")
        else:
            out.append(f"  {line}")
    return out


def main() -> None:
    p = argparse.ArgumentParser(description="vim の undo の履歴から変更ごとの版を時刻つきで取り出す")
    p.add_argument("file", type=Path)
    p.add_argument("--out", type=Path, required=True, help="書き出し先（リポジトリの外。scratchpad など）")
    p.add_argument("--undodir", type=Path, default=Path.home() / ".vim/undo")
    p.add_argument("--from", dest="from_", metavar="HH:MM", help="この時刻以降の変更だけ")
    p.add_argument("--to", metavar="HH:MM", help="この時刻までの変更だけ")
    args = p.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", newline="\n")
    sys.stderr.reconfigure(encoding="utf-8", newline="\n")

    if not shutil.which("vim"):
        sys.exit("vim がありません（編集したのと同じ環境で動かす）")
    src = args.file.resolve()
    if not src.is_file():
        sys.exit(f"{args.file}: ファイルがありません")
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        rows = dump_history(src, args.undodir.expanduser(), work)
        if not rows:
            sys.exit(f"{src}: undo の履歴がありません（undofile が無効だった・vim の外で書き換えた・パスが違う）")
        text = {}
        for seq in [0] + [r[0] for r in rows]:
            lines = (work / f"{seq}.txt").read_text(encoding="utf-8").splitlines()
            text[seq] = [] if lines == [""] else lines  # vim は空のバッファも空行 1 つで書き出す
        dst = args.out / src.name
        dst.mkdir(parents=True, exist_ok=True)
        report = [f"{src}  変更 {len(rows)} 件"
                  f"（{rows[0][2]:%Y-%m-%d %H:%M:%S} 〜 {rows[-1][2]:%H:%M:%S}）", ""]
        written = 0
        for seq, parent, when, save in rows:
            if clock_match(when, args.from_, True) and clock_match(when, args.to, False):
                tag = f"_s{save}" if save else ""
                (dst / f"{when:%Y%m%d-%H%M%S}_u{seq:04d}{tag}{src.suffix}").write_text(
                    "".join(f"{line}\n" for line in text[seq]), encoding="utf-8", newline="\n")
                head = f"{when:%H:%M:%S}  u{seq}" + (f"  保存{save}" if save else "")
                if parent != seq - 1:  # undo で戻ってから書いた枝
                    head += f"  （u{parent} に戻ってから）"
                report += [head, *describe(text[parent], text[seq]), ""]
                written += 1
    (dst / "changes.txt").write_text("\n".join(report), encoding="utf-8", newline="\n")
    print(f"{written} 版 → {dst}（差分の一覧は changes.txt）")


if __name__ == "__main__":
    main()
