from collections import deque

def bfs_shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    start = (0, 0)
    goal = (rows - 1, cols - 1)

    if grid[0][0] == 1 or grid[goal[0]][goal[1]] == 1:
        return -1  # start or end is blocked

    directions = [(1,0), (-1,0), (0,1), (0,-1)]  # Down, Up, Right, Left
    visited = [[False]*cols for _ in range(rows)]
    queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
    visited[0][0] = True

    while queue:
        r, c, dist = queue.popleft()

        if (r, c) == goal:
            return dist  # shortest path length found

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if not visited[nr][nc] and grid[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist + 1))

    return -1  # no path found

# Example grid
grid = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

result = bfs_shortest_path(grid)
print("Shortest path length:", result)
