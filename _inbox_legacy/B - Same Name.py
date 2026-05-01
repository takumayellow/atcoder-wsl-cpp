n = int(input())  # 数の入力
s, t = [], []  # 名前を格納するためのリスト

for _ in range(n):
    a, b = input().split()  # 名前をそのまま受け取る
    s.append(a)
    t.append(b)

# ここからは以前のコードと同様に処理すればOK
for i in range(n):
    for j in range(i + 1, n):
        if s[i] == s[j] and t[i] == t[j]:
            print("Yes")
            exit()
print("No")
