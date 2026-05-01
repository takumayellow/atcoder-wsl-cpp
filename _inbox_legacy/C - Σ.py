n, k = map(int, input().split())
a = set(map(int, input().split()))

# 1からkまでの整数の和は公式を使って計算
total_sum = k * (k + 1) // 2

# aに含まれる1からkまでの数の和を引く
a_sum = sum(x for x in a if x <= k)

# 最終的に残る部分の和
print(total_sum - a_sum)