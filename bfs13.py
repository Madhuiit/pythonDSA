from collections import deque

def shortestPath(grid, k):
    rows, cols = len(grid), len(grid[0])
    visited = [[-1] * cols for _ in range(rows)]
    queue = deque()
    queue.append((0, 0, 0, 0))  # (row, col, steps, obstacles_removed)

    while queue:
        r, c, steps, removed = queue.popleft()

        # Out of bounds
        if r < 0 or r >= rows or c < 0 or c >= cols:
            continue

        # If obstacle and no removals left
        if grid[r][c] == 1:
            removed += 1

        if removed > k:
            continue

        # If already visited with better or same k
        if visited[r][c] != -1 and visited[r][c] <= removed:
            continue

        # Mark visited with the least obstacles used
        visited[r][c] = removed

        # If destination
        if r == rows - 1 and c == cols - 1:
            return steps

        # Explore 4 directions
        for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
            queue.append((r + dr, c + dc, steps + 1, removed))

    return -1

grid = [
  [0,1,1],
  [1,1,0],
  [1,0,0]
]
k = 1
print(shortestPath(grid,k))
