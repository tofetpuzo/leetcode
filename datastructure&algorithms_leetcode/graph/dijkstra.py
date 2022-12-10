def dijkstra(graph, start, goal):
    shortest_distance = {}
    track_predecessor = {}
    unseenNodes = graph 
    inf = float("inf")
    track_path = []
    
    for node in unseenNodes:
        shortest_distance[node] = inf
        
    shortest_distance[start] = 0
     
    while unseenNodes:
        min_distance_node = None
        
        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node
        
        path_options = graph[min_distance_node].items()
        
        for child_node , weight in path_options:
            if shortest_distance[min_distance_node]  + weight < shortest_distance[child_node]:
               shortest_distance[child_node]  = shortest_distance[min_distance_node] + weight
               track_predecessor[child_node] = min_distance_node
    
    unseenNodes.pop(min_distance_node)
    
    currentNode = goal
    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            print("Path is not optimised")          
            break
    
    track_path.insert(0, start)
    
    if shortest_distance[goal] != inf:
        print("shortest distance is " + str(shortest_distance[goal]))
        print("Optimal path is " +  str(track_path))