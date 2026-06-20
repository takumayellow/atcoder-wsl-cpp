# ICPC 2014 国内予選 A: Tax Rate Changed (AOJ 1192)
# 複数データセット入力（パターンB: 先頭行が複数値・"0 0 0" で終端）
import sys
input = lambda: sys.stdin.readline().rstrip("\n")


def main():
    while True:
        x, y, s = map(int, input().split())
        if x == 0 and y == 0 and s == 0:   # 番兵。計算・出力せず終了
            break

        ans = 0
        for a in range(1, s):
            for b in range(1, s):
                if ((100 + x) * a) // 100 + ((100 + x) * b) // 100 == s:
                    t = ((100 + y) * a) // 100 + ((100 + y) * b) // 100
                    if t > ans:
                        ans = t
        print(ans)


main()
