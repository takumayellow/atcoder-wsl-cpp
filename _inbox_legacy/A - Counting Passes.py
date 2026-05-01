n, l = map(int, input().split())  # 小文字の 'l' を使用
a = list(map(int, input().split()))
k = 0

for i in range(n):
    if a[i] >= l:  # 小文字の 'l' を使用
        k += 1  # カウンタを増やす

print(k)
