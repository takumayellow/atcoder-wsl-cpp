import sys

input = sys.stdin.readline

q = int(input())
s = input().strip()
t = input().strip()
n, m = len(s), len(t)

# nxt[i]: i 以降で最初に T が始まる位置（無ければ n）
# |T| <= 10 なので各位置での一致判定は s[i:i+m] == t で O(|T|)
nxt = [n] * (n + 1)
for i in range(n - 1, -1, -1):
    nxt[i] = i if s[i:i + m] == t else nxt[i + 1]

out = []
for _ in range(q):
    L, R = map(int, input().split())
    # L-1 以降で最初の出現が R までに収まっていれば Yes
    out.append("Yes" if nxt[L - 1] + m <= R else "No")
print("\n".join(out))
