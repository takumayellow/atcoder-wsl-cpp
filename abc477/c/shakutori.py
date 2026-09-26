# ABC477 C - Range Search Query
# https://atcoder.jp/contests/abc477/tasks/abc477_c
# 解法: 尺取り法で「左端 l ごとの T を含む最小の右端 f(l)」を求め、クエリは R >= f(L) で判定
# 計算量: O(|S|·|T| + Q)
# 詳しくは explanation.md / slides.pdf を参照
import sys

input = sys.stdin.readline

q = int(input())  # 入力は Q が先頭、その後に S, T
s = input().strip()
t = input().strip()
n, m = len(s), len(t)

# f[l]: 左端 l(0-indexed) で T を含む最小の右端(1-indexed)。無理なら n+1
# [l, r] が T を含むなら l を右にずらすと f は単調非減少 → 尺取りで r を戻さない
f = [n + 1] * n  # n+1 は「どの R(<= n) でも足りない」番兵
cnt = 0  # 窓 s[l:r] に完全に収まっている T の出現数
r = 0  # 窓は半開区間 s[l:r]。r はそのまま 1-indexed の右端として使える
for l in range(n):
    # ここで r を l の近くに戻さないのが尺取り法。r は全体で n 回しか進まない
    while r < n and cnt == 0:
        r += 1
        if r - m >= l and s[r - m:r] == t:  # 右端 r で終わる出現を足す
            cnt += 1
    if cnt > 0:
        f[l] = r
    if l + m <= r and s[l:l + m] == t:  # 左端 l から始まる出現を外す（窓内にあるものだけ）
        cnt -= 1

out = []
for _ in range(q):
    L, R = map(int, input().split())
    out.append("Yes" if f[L - 1] <= R else "No")  # l は 0-indexed なので L-1
print("\n".join(out))
