def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for i in graph[start]:
        if i not in visited:
            dfs(graph, i, visited)

    return visited
    


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("\nDFS Traversal: ")
dfs(graph, 'A')