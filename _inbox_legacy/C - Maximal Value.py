n = int(input())  # 整数nを入力
b = list(map(int, input().split()))  # スペース区切りで整数を入力し、リストに変換
print(sum(b) + max(b))  # リストの合計と最大値を足して出力