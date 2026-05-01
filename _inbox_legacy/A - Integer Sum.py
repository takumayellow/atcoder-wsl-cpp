n = int(input())  # リストの要素数を入力から受け取る（コード内で使用しない）
a = list(map(int, input().split()))  # 整数のリストを入力から受け取る

# リスト `a` のすべての要素を合計する
print(sum(a))