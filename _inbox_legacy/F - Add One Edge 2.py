import sys
from collections import defaultdict, deque

# Input parsing
N = int(input())
edges = [tuple(map(int, input().split())) for _ in range(N - 1)]

# Build adjacency list and initialize degrees
adj = defaultdict(list)
degree = [0] * (N + 1)
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)
    degree[u] += 1
    degree[v] += 1

# BFS to determine the depth of each node
def bfs(start):
    queue = deque([start])
    parent = [-1] * (N + 1)
    depth = [0] * (N + 1)
    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if neighbor != parent[node]:  # Avoid revisiting the parent
                parent[neighbor] = node
                depth[neighbor] = depth[node] + 1
                queue.append(neighbor)
    return parent, depth

# Run BFS from an arbitrary node to find the farthest node
parent, depth = bfs(1)
farthest = depth.index(max(depth))  # Find the node with the maximum depth

# Run BFS from the farthest node to get the diameter end-points and path
parent, depth = bfs(farthest)
other_end = depth.index(max(depth))  # The other end of the diameter
diameter_path = []
node = other_end
while node != -1:
    diameter_path.append(node)
    node = parent[node]

# Determine if adding an edge between any two nodes in the path results in degree 3
cycle_count = 0
degree_two_nodes = [node for node in diameter_path if degree[node] == 2]

# Check each pair of degree-2 nodes
cycle_count = 0
for i in range(len(degree_two_nodes)):
    for j in range(i + 1, len(degree_two_nodes)):
        # Each pair of degree-2 nodes can form a valid cycle when connected
        cycle_count += 1

print(cycle_count)
