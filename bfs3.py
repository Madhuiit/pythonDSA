from collections import deque

def num_island(grid):
    if not grid:
        return 0
    rows,cols = len(grid),len(grid[0])
    visited = set()

    island_count = 0

    def bfs(r,c):
        queue = deque([(r,c)])
        visited.add((r,c))

        while queue:
            x,y= queue.popleft()
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx,ny = x+dx,y+dy

                if (0<=nx <rows and 0<= ny <cols and grid[nx][ny]=="1" and (nx,ny) not in visited ):
                    queue.append((nx,ny))
                    visited.add((nx,ny))
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visited:
                bfs(r,c)

                island_count +=1
    return island_count



grid = [
    ['1','1','0','0'],
    ['0','1','0','0'],
    ['0','0','1','0'],
    ['1','0','0','1']
]


print("Number of island" , num_island(grid))