# ICPC 国内予選 雛形（Python3）: 複数データセットを番兵までループ
#
# 入力は AtCoder と違い「1ファイルに複数データセットが連結」。番兵が来るまで回す。
# 書き換えるのは「先頭の読み方」と「番兵の条件」の2か所だけ。input() で十分。
#
#   先頭が複数値:  a, b, s = map(int, input().split())   番兵 if a == b == s == 0: break
#   1行にn個:      a = list(map(int, input().split()))
#   個数T先頭(番兵なし): for _ in range(int(input())): ...

while True:
    n = int(input())          # ← 先頭を読む（問題ごとに変更）
    if n == 0:                # ← 番兵（問題ごとに変更）
        break

    # ... 1データセットを解いて ans を作る ...
    ans = 0
    print(ans)                # 1データセット = 1行
