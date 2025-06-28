from collections import deque
def shortes_path_bfs(grid):
    if not grid  or grid[0][0]=="1":
        return -1 
    
    n = len(grid)
    m = len(grid[0])
    #directions up down ,left ,right 
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    queue = deque()
    queue.append((0,0,1)) # starting from (0,0) with count 1

    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    while queue :
        row ,col ,dist = queue.popleft()
        # check if destination is reached 
        if row == n-1  and col == m-1:
            return dist
        for dr ,dc in directions:
            new_r , new_c = row+dr , col+dc
            if (0<=new_r < n and 0<= new_c < m and not  visited[new_r][new_c] and grid[new_r][new_c] == "0"):
                visited[new_r][new_c] = True
                queue.append((new_r,new_c,dist +1))
    return -1


#it simply mean that destination is not reachble









# from collections import deque
# def shortest_path_bfs(grid):
#     if not grid or grid[0][0]=="1":
#         return -1
    

#     n = len(grid)
#     m = len(grid[0])

#     # direction up down ,left right 

#     directions = [(-1,0),(1,0),(0,-1),(0,1)]

#     queue = deque()
#     queue.append((0,0,1)) #starting at (0,0) with count 1

#     visited = [[False]*m for _ in range(n)]
#     visited[0][0]=True
#     while queue:
#         row ,col , dist = queue.popleft()

#         #check if destination is reached 
#         if row == n-1 and col == m-1:
#             return dist
        
#         for dr ,dc in directions:
#             new_r,new_c = row+dr ,col+dc 

#             if (0<=new_r <n and 0 <= new_c < m and not visited[new_r][new_c] and grid[new_r][new_c]=="0"):
#                 visited[new_r][new_c] = True
#                 queue.append((new_r,new_c,dist+1))
#     return -1 #it simply mean  destination is not reachesble
grid = [
  ['0', '0', '1', '0'],
  ['1', '0', '1', '0'],
  ['0', '0', '0', '0'],
  ['0', '1', '1', '0']
]

result = shortes_path_bfs(grid)
print("Shortest path lengeth",result)



        


    

