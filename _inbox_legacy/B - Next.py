n = int(input())  # 数値の個数
a = list(map(int, input().split()))  # リストに数値を格納

max_value = max(a)  # リスト中の最大値を取得
b = [x for x in a if x != max_value]  # 最大値以外の要素だけを残す

print(max(b))  # 最大値が消されたリストを出力