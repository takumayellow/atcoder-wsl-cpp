n, x = map(int, input().split())
a = list(map(int, input().split()))

# 値 x のインデックスを収集する
indices_to_remove = [i for i, value in enumerate(a) if value == x]

# インデックスを逆順で削除する
for index in reversed(indices_to_remove):
    a.pop(index)

print(*a)