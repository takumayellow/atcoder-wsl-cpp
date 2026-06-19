# ICPC 複数データセット入力の雛形（Python 3）
#
# ICPC は AtCoder と違い「1ファイルに複数データセット」が定番。
# 終端条件は問題ごとに違う。下の A/B/C から問題文に合うものを使う:
#   A) 番兵終端: n が 0（や "0 0"）の行で終わり          ← 国内予選で最頻出
#   B) EOF 終端: 入力が尽きるまで繰り返し
#   C) ケース数: 先頭に T があり、T 個のデータセット
#
# 注意:
#   - NumPy は実質使えない（同梱コンパイル不可・ジャッジ非搭載前提）。素の Python 3 で書く。
#   - 自前ライブラリは library/py/ から貼り付けるか import せずに本文へコピペ。

import sys
input = sys.stdin.readline          # 高速入力（行単位）。複数値は .split() で。


def solve(n):
    # ... 残りの入力を読んで答えを出力 ...
    pass


def main():
    # ===== パターンA: 番兵終端（n==0 で終了）=====
    while True:
        line = input()
        if not line:                # 念のため EOF も止める
            break
        n = int(line)
        if n == 0:
            break
        solve(n)

    # ===== パターンB: EOF 終端 =====
    # for line in sys.stdin:
    #     a, b = map(int, line.split())
    #     ...

    # ===== パターンC: 先頭にケース数 T =====
    # t = int(input())
    # for _ in range(t):
    #     ...


main()
