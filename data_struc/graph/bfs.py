def bfs(graph, root):
    queue = []
    visited = [False] * len(graph.data)
    
    visited[root] =  True
    queue.append(root)
    index = 0
    
    while index < len(queue):
        current = queue[index]
        index +=1
        # check all edges of current
        for node in graph.data[current]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)
    return queue