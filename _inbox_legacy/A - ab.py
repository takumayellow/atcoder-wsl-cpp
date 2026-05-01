n = int(input())
s = input()

# sの中で隣り合う 'a' と 'b' または 'b' と 'a' があるかをチェック
for i in range(n-1):
    if (s[i] == 'a' and s[i+1] == 'b') or (s[i] == 'b' and s[i+1] == 'a'):
        print("Yes")
        break
else:
    print("No")
