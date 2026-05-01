n = int(input())
a = list(map(int, input().split()))
b = []

for i in range(n):
    ai = sum(a[7*i:7*i+7])  # 7つの数字を合計する方法
    b.append(ai)  # リストに値を追加する

print(" ".join(map(str, b)))  # 整数リストを文字列に変換して表示する