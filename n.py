import time
import os
from collections import deque

# Input grid
grid = [
    ['1', '1', '0', '0'],
    ['0', '1', '0', '0'],
    ['0', '0', '1', '0'],
    ['1', '0', '0', '1']
]

rows = len(grid)
cols = len(grid[0])
visited = set()

# Emoji map for nicer output (fall back to numbers if needed)
def symbol(n):
    return f"{n}️⃣" if n <= 9 else str(n)

# Print grid with island numbers
def print_grid(marked):
    os.system('cls' if os.name == 'nt' else 'clear')
    for r in range(rows):
        row = ""
        for c in range(cols):
            if (r, c) in marked:
                row += f" {symbol(marked[(r,c)])} "
            else:
                row += f" 0 " if grid[r][c] == '0' else " 1 "
        print(row)
    print()

# BFS function
def bfs(start_r, start_c, island_id, marked):
    queue = deque()
    queue.append((start_r, start_c))
    visited.add((start_r, start_c))
    marked[(start_r, start_c)] = island_id

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < rows and 0 <= nc < cols and
                grid[nr][nc] == '1' and (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                queue.append((nr, nc))
                marked[(nr, nc)] = island_id
                print_grid(marked)
                time.sleep(0.7)

# Main animation logic
def animate_island_discovery():
    marked = {}
    island_count = 0
    print("Initial Grid:\n")
    print_grid(marked)
    time.sleep(1.5)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                island_count += 1
                bfs(r, c, island_count, marked)
                print(f"Finished Island {island_count}!")
                time.sleep(1.5)

    print(f"\n✅ Total Islands: {island_count}")

# Run the animation
animate_island_discovery()
