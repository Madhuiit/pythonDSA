


from collections import deque

def bfs_grid(grid, start):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([start])

    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right

    while queue:
        r, c = queue.popleft()

        if (r, c) in visited:
            continue

        visited.add((r, c))
        print(f"Visited cell ({r}, {c})")

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                queue.append((nr, nc))

grid = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 1, 1, 1]
]

bfs_grid(grid, (0, 0))
