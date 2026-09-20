# ABC476 C - 3rd Largest（Python 版。考え方の詳細は main.cpp のコメント参照）
#
# 上位 3 個だけを持ち歩き、新要素を足して降順 3 番目を答える O(N) 解法。
# ただし Python だと N = 5e5 でこのループは重く、TLE のおそれがある
# （その場合は main.cpp を提出する）。

n = int(input())
a = list(map(int, input().split()))

# 先頭 3 個ぶん。昇順に持つので s[-3] が「降順 3 番目」= 最小要素。
s = sorted(a[:3])
print(s[-3])

for k in range(3, n):
    s.append(a[k])   # 上位 3 個 + 新要素 = 4 個
    s = sorted(s)
    s = s[-3:]       # 最小を切り捨てて上位 3 個に戻す（昇順のまま保持）
    print(s[-3])
