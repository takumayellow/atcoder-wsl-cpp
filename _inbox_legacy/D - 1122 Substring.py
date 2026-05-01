from collections import defaultdict

# 入力
n = int(input())
a = list(map(int, input().split()))

# 初期化
count = defaultdict(int)  # 要素の出現回数を記録
left = 0  # スライディングウィンドウの左端
max_length = 0  # 1122 数列の最大長さ

# 右端をスライド
for right in range(n):
    count[a[right]] += 1  # 右端の要素をカウント

    # 条件を満たさなくなったら左端をスライド
    while any(count[x] > 2 for x in count):
        count[a[left]] -= 1
        if count[a[left]] == 0:
            del count[a[left]]
        left += 1

    # 現在のウィンドウが 1122 数列か確認
    if all(val == 2 for val in count.values()):
        max_length = max(max_length, right - left + 1)

# 結果を出力
print(max_length)
