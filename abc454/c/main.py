import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        g[a].append(b)

    seen = [False] * (n + 1)
    seen[1] = True
    q = deque([1])
    ans = 0
    while q:
        u = q.popleft()
        ans += 1
        for v in g[u]:
            if not seen[v]:
                seen[v] = True
                q.append(v)

    print(ans)

if __name__ == "__main__":
    main()
