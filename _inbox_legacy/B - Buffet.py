n = int(input())  # 整数の入力
a = list(map(int, input().split()))  # リストaの入力
b = list(map(int, input().split()))  # リストbの入力
c = list(map(int, input().split()))  # リストcの入力

ans = sum(b)  # bの総和を計算

# 連続した料理の間で追加満足度を足す
for i in range(n - 1):
    if a[i + 1] == a[i] + 1:
        ans += c[a[i] - 1]

print(ans)  # 結果を表示