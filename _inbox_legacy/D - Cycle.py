from collections import deque, defaultdict

def find_shortest_cycle(N, M, edges):
    graph = defaultdict(list)
    
    # グラフの隣接リスト作成
    for u, v in edges:
        graph[u].append(v)
    
    # BFSでサイクル検出
    def bfs(start):
        dist = [-1] * (N + 1)  # 各頂点の距離
        parent = [-1] * (N + 1)  # 親頂点
        dist[start] = 0
        
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                if dist[neighbor] == -1:  # 未訪問の頂点
                    dist[neighbor] = dist[node] + 1
                    parent[neighbor] = node
                    queue.append(neighbor)
                elif neighbor != parent[node]:  # サイクルが検出された
                    # サイクルの長さを計算
                    cycle_length = dist[node] + dist[neighbor] + 1
                    if neighbor == 1 or node == 1:  # 頂点1を含むかどうか
                        return cycle_length
        
        return -1  # サイクルがない場合
    
    # 頂点1から探索を始める
    return bfs(1)

# 入力
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# サイクルの長さを出力
result = find_shortest_cycle(N, M, edges)
print(result)
