# ABC476 D - Automat（ドリンクの本数を全探索する版。explained.py と同じ方針）
#
# ドリンクを安い順に 0, 1, 2, ... 本買う場合をすべて試し、
# 各ケースで「残った総額で買えるデザートの個数」を累積和 + 二分探索で求める。
# 商品を 1 つの袋にまとめてしまう main.cpp とは別ルートだが、答えは一致する。
# 計算量 O(N log N + M log M)。

from bisect import bisect

n, m, k = map(int,input().split())
x, y = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

# デザートを安い順に並べた累積和 aa（aa[i] = 安い方から i+1 個の合計金額）。
# 単調増加なので「予算以下の要素数」= 買える個数 を二分探索で取り出せる。
a.sort()
aa = [0]
for a in a:
    aa.append(aa[-1]+a)
aa=aa[1:]

# 先頭にダミーの 0 を置くことで、ループ 1 週目が「ドリンク 0 本」の場合になる。
b.sort()
b = [0] + b

ans = 0
r = len(aa)         # 買えるデザートの個数（ドリンクを買うほど単調に減るので探索上限に使う）
s = x + y * k       # 所持金の総額。買い物のたびに価格ぶんだけ減る
for ib in range(len(b)):
    yi = (b[ib] + k -1) // k    # このドリンクに必要な K ドル札の枚数 = ceil(b/k)
    if yi > y:
        # K ドル札が足りない。b は昇順なので以降はさらに買えない → 打ち切り
        break
    y -= yi
    s -= b[ib]
    # 上限に r を渡しているのがポイント。r は減る一方なので、探索範囲が広がらない。
    r = bisect(aa, s, 0, r)
    ans = max(ans, r+ib)        # ドリンク ib 本 + デザート r 個

print(ans)
