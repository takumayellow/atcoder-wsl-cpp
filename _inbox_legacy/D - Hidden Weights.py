def dfs(v, value, graph, values):
    values[v] = value
    for u, w in graph[v]:
        if values[u] is None:
            dfs(u, value + w, graph, values)

def solve():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    
    for _ in range(M):
        u, v, w = map(int, input().split())
        u -= 1  # 0-indexed に変換
        v -= 1  # 0-indexed に変換
        graph[u].append((v, w))
        graph[v].append((u, -w))  # 逆方向の重みを負にする

    values = [None] * N
    
    for i in range(N):
        if values[i] is None:
            dfs(i, 0, graph, values)
    
    print(" ".join(map(str, values)))

solve()