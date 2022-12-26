from typing import List


tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
ticket = [["JFK", "SFO"], ["JFK" ,"ATL"], ["SFO", "ATL"], ["ATL", "JFK"],["ATL", "SFO"]]

# ouput = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
def reconstructItineray(tickets: List[List[str]]):
    adj = {src : [] for src , _ in tickets}
    
    tickets.sort()
    for src , dist in tickets:
        adj[src].append(dist)
        
    res = ["JFK"]
    def dfs(src):
        if len(res) == len(ticket) + 1:
            return True
        
        if src not in adj:
            return False
        
        temp = list(adj[src])
        for node , nei in enumerate(temp):
            adj[src].pop(node)
            res.append(nei)
            
            if dfs(nei): return True
            
            adj[src].insert(node,nei)
            res.pop()
            
        return True
    
    dfs("JFK")
    return res
            
print(reconstructItineray(ticket))       
            # if we choose a path that is invalid like jfk -> atl instead of jfk -> sfo
            
            
        
        
    