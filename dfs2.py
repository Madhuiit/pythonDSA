def has_cycle(graph):
    visited = set()

    def  dfs(node,parent):
        visited.add(node)


        for neighbor in graph.get(node , []):
            if neighbor not in visited:
                if dfs(neighbor,node):
                    return True
            elif neighbor != parent :
                return True
            
        return False
    
    for node  in graph :
        if node not in visited:
            if dfs(node , -1):
                return True
    return False

graph1 = {
    0: [1],
    1: [0, 2],
    2: [1]
}
print(has_cycle(graph1))  # False — no cycle

graph2 = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}
print(has_cycle(graph2))  # True — 0-1-2-0


