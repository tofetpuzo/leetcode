# reorder routes to make all paths lead to the city zero

from typing import List

def minReorder(n: int, connections: List[List[int]]) -> int:
    # start at city 0
    # recursively check its neighbors
    # count outgoing edges
    edges = {(a, b) for a, b in connections}
    neighbors = { city: [] for city in range(n)}
    visit = set()
    changes = 0
    
    for a, b in connections:
        neighbors[a].append(b)
        neighbors[b].append(a)
        
    def dfs(city):
        nonlocal edges, neighbors , visit , changes
        for nei in neighbors[city]:
            if nei in visit:
                continue
            # check if this neighbor can reach city 0
            if (nei, city) not in edges:
                changes+=1
                
            visit.add(nei)
            dfs(nei)
            
    visit.add(0)
    dfs(0)
    
    return changes
                
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]   
n = 6
print(minReorder(n, connections))       