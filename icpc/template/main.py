# ICPC 国内予選 複数データセット雛形（Python 3 / トークンストリーム読み）
#
# 使い方は3か所だけ:
#   (1) 先頭行ぶんを rd(...) / ri() で読む
#   (2) 番兵（全部 0 など）で break
#   (3) 残りが必要なら rd(...) を足し、print で「1データセット=1行」出力
#
# 入力パターン(A:単一値0終端 / B:複数値0終端 / C:先頭にデータ数T)の詳細は
#   icpc/template/README.md を参照。トークン読みなので行の切れ方に依存しない。
import sys

_tok = iter(sys.stdin.buffer.read().split())
def ri():    return int(next(_tok))                       # 整数1個
def rd(n):   return [int(next(_tok)) for _ in range(n)]   # 整数n個
def rs(n=1): return [next(_tok).decode() for _ in range(n)]  # 文字列n個


def main():
    while True:
        x, y, s = rd(3)              # ← 先頭行ぶんを読む（問題ごとに変更）
        if (x, y, s) == (0, 0, 0):   # ← 番兵（問題ごとに変更）
            break

        # 残りが必要なら rd(...) で読む。例: a = rd(n)
        ans = 0
        # ... ここに解法を書く ...
        print(ans)


main()
