from collections import deque
def orangesRotten(grid):
    rows ,cols = len(grid),len(grid[0])

    queue = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]== 2:
                queue.append((r,c,0)) # (row ,col,minute)

            elif grid[r][c] == 1:
                fresh += 1
    time = 0
    while queue:
        r,c,t = queue.popleft()
        time = max(time , t) 
        for dr ,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc = r + dr , c+ dc

            if (0<=nr <rows and 0 <= nc < cols and grid[nr][nc]==1):

                grid[nr][nc]=2
                fresh -= 1



                queue.append((nr,nc,t+1))

    return time if fresh == 0 else -1








grid = [
  [2,1,1],
  [1,1,0],
  [0,1,1]
]
print(orangesRotten(grid))