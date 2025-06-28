def topological_sort(graph):
    visited = set()
    stack = []


    def dfs(node):
        visited.add(node)
        for  neighbor in graph.get(node,[]):
            if neighbor not in visited :
                dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited :
            dfs(node)

    return stack[::-1] # reverse the stack


graph = {
    5: [2, 0],
    4: [0, 1],
    2: [3],
    3: [1],
    1: [],
    0: []
}

print(topological_sort(graph))


