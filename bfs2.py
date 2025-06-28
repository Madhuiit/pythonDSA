from collections import deque
def bfs_shortest_path(graph,start):
    visited = set()
    distance = {start:0}
    queue=deque([start])

    while queue:
        node = queue.popleft()
        print(f"Visited {node} at distance {distance[node]}")
        visited.add(node)
        for neighbor in  graph[node]:
            if neighbor not in visited and neighbor not in distance:
                queue.append(neighbor)
                distance[neighbor]= distance[node]+1


# from collections import deque
# def bfs_shortest_path(graph,start):
#     visited = set()

#     distance = {start:0}
#     queue=deque([start])

#     while queue:
#         node = queue.popleft()
#         print(f"Visited {node} at distence {distance[node]}")
#         visited .add(node)
#         for neighbor in graph[node]:
#             if neighbor not in visited and neighbor not in distance:
#                 queue.append(neighbor)
#                 distance[neighbor] = distance[node]+1




graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(bfs_shortest_path(graph,"A"))