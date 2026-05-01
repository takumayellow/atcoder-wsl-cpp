n = int(input())
s = [input().strip() for _ in range(n)]  # .strip() で空白を取り除く

for i in range(n-2):
    if s[i] == "sweet" and s[i+1] == "sweet":  # 連続する sweet をチェック
        print("No")
        break
else:
    print("Yes")  # 連続した "sweet" がなければ Yes
