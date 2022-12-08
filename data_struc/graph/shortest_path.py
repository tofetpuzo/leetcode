import queue



def shortest_path(graph, source, target):
    visited = [False] * len(graph.data)
    distance = [float("inf")] * len(graph.data)
    queue = []
    
    distance[source] = 0
    queue.append(source)
    
    idx = 0
    while idx < len(queue) and not visited[target]:
        current = queue[idx]
        idx +=1
        visited[current] = True
        
    
