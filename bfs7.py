from collections import deque, defaultdict

def bfs_shortest_path(routes, start, end):
    # Build the graph
    graph = defaultdict(list)
    for src, dest in routes:
        graph[src].append(dest)
        graph[dest].append(src)  # Assuming flights are two-way

    visited = set()
    queue = deque([(start, 0)])  # (city, steps)

    while queue:
        current_city, steps = queue.popleft()
        
        if current_city == end:
            return steps  # Found the destination
        
        visited.add(current_city)

        for neighbor in graph[current_city]:
            if neighbor not in visited:
                queue.append((neighbor, steps + 1))
                visited.add(neighbor)

    return -1  # No path found

# Example usage:
routes = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"), ("D", "F"), ("E", "F")]
start = "A"
end = "F"

print("Shortest number of flights:", bfs_shortest_path(routes, start, end))
