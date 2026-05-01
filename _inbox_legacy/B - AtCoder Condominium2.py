n, k = map(int, input().split())

# 3桁の数字を生成してリストに追加する
numbers = []
for i in range(1, n + 1):
    for j in range(1, k + 1):
        number = f"{i}0{j}"  # 例: "101", "102", ...
        numbers.append(number)

# 列ごとのリストに分解する
a = []
b = []
for number in numbers:
    a.append(int(number[0]))  # 先頭の1桁
    b.append(int(number[2]))  # 最後の1桁

# 計算する
results = [100 * ai + bi for ai, bi in zip(a, b)]

# 結果を表示
print(sum(results))