n, x = map(int, input().split())
a = list(map(int, input().split()))

# 新しいリストを作成して x を除外する
filtered_a = [value for value in a if value != x]

print(*filtered_a)