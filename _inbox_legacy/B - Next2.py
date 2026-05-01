n = int(input())  # 数値の個数
a = list(map(int, input().split()))  # リストに数値を格納

max_value = max(a)  # 最大値を取得
while max_value in a:
    a.pop(a.index(max_value))  # 最大値のインデックスを取得して削除

print(max(a))  # 最大値が消されたリストを出力