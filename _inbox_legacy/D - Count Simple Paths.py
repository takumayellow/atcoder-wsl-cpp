H, W, K = map(int, input().split())
S = [input().strip() for _ in range(H)]

# Directions for movement: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
total_paths = 0

# DFS function to count paths of length exactly K
def dfs(x, y, steps, visited):
    global total_paths
    # If we have reached exactly K steps, count this path as valid
    if steps == K:
        total_paths += 1
        return
    
    # Explore all four possible directions
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '.' and (nx, ny) not in visited:
            visited.add((nx, ny))
            dfs(nx, ny, steps + 1, visited)
            visited.remove((nx, ny))

# Start DFS from each empty cell in the grid
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            # Initialize DFS from each open cell
            dfs(i, j, 0, {(i, j)})

# Output the total number of valid paths
print(total_paths)
