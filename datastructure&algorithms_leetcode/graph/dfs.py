def dfs(graph, root):
    stack = []
    visited = [False] * len(graph.data)
    parent = [None] * len(graph.data)
    stack.append(root)
    result = []
    
    while len(stack) > 0:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            result.append(current)
            for node in graph.data[current]:
                parent[node] = current
                if not visited[node]:
                    stack.append(node)
                
    return result  