# 自然数 N を取得
n = int(input())

# 合成ルールを格納するリスト（1-indexed）
a = [[0] * (n + 1) for _ in range(n + 1)]

# 各段のデータを読み取り、2次元配列 a に格納する
for j in range(1, n + 1):
    row_data = list(map(int, input().split()))
    for i in range(j):
        a[j][i + 1] = row_data[i]
        a[i + 1][j] = row_data[i]

# データの確認（デバッグ用）
print("a 配列の内容:")
for row in a[1:]:
    print(row)

# 元素 1 から始めて、順に合成する
current_element = 1
for i in range(2, n + 1):
    current_element = a[current_element][i]

# 最終的に得られる元素を出力
print(f"最終的に得られる元素: {current_element}")
