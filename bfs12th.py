from collections import deque

def is_valid(x, y, N, visited):
    return 0 <= x < N and 0 <= y < N and not visited[x][y]

def knight_min_steps(N, start, end):
    # 8 possible knight moves
    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    
    visited = [[False]*N for _ in range(N)]
    queue = deque()
    
    # queue: (x, y, steps)
    queue.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == end:
            return steps

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, N, visited):
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, steps + 1))
    
    return -1  # If not reachable

# Example Usage
N = 8
start = (0, 0)
end = (7, 7)
print("Minimum steps:", knight_min_steps(N, start, end))
