import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def bfs(start, graph, visited):
    connected = []
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        connected.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return connected

def main():
    N, Q = map(int, input().split())
    graph = defaultdict(set)
    results = []

    for _ in range(Q):
        query = list(map(int, input().split()))
        
        if query[0] == 1:
            _, u, v = query
            graph[u].add(v)
            graph[v].add(u)

        elif query[0] == 2:
            _, v, k = query
            visited = set()
            connected_vertices = bfs(v, graph, visited)
            connected_vertices.sort(reverse=True)

            if len(connected_vertices) < k:
                results.append(-1)
            else:
                results.append(connected_vertices[k - 1])

    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()
