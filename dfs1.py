def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        # Base case: if out of bounds or water
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        
        # Mark this cell as visited (sink the island)
        grid[r][c] = '0'
        
        # Explore all 4 directions
        dfs(r+1, c)  # down
        dfs(r-1, c)  # up
        dfs(r, c+1)  # right
        dfs(r, c-1)  # left

    # Main logic to count islands
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)  # Launch DFS to sink the island

    return count



grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]

]

print(numIslands(grid))
