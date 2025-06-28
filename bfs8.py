from collections import deque

def orangesRotten(grid):
    rows,cols = len(grid),len(grid[0])

    queue = deque()
    fresh = 0

    #add all  rotten oranges to the queue ,count fresh ones 

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]==2:
                queue.append((r,c,0)) 
            elif grid[r][c]== 1:
                fresh+=1

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    minutes = 0

    while queue:
        r,c, time = queue.popleft()

        minutes = max(minutes,time)

        for dr ,dc in directions:
            nr ,nc = r+dr , c+dc
            #if in bounds and orange is fresh
            if 0<= nr< rows and 0<=nc < cols and grid[nr][nc]== 1:
                grid[nr][nc]=2
                fresh -= 1
                queue.append((nr,nc,time+1))
    return minutes if fresh == 0 else -1


grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
print(orangesRotten(grid))  # Output: 4




