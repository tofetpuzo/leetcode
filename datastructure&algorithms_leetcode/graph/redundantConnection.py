# In this problem, a tree in an undirected graph that is connected 
# has no cycles. You are given a graph that stareted as a tree with 
# n nodes labeled from 1 to n, and was not an edge that already 
# existed. The graph is represented as an array edges of length
# n where edges[i] = [a, b] indicates that there is an edge between 
#  nodes a(i) and b(i) in the graph
# return an edge that can be removed so that 
# the resulting graph is a tree of n nodes. 
# if there are multip;e answers, return the answer that occurs last
#  in the input.
# edges = [[1, 2], [1, 3], [2, 3]]

from typing import List


def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    parent = [i for i in range(len(edges) + 1)]
    rank = [1] * (len(edges) + 1)
    
    # This helps find the parent of any node this allows to build the 
    # tree 
    def find(any_node):
        p = parent[any_node]
        
        while p != parent[p]:
             parent[p] = parent[parent[p]] 
             p = parent[p] 
        return p
    
    # return False if can not complete
    def union(node1, node2):
        # to union them we have to find both of their roots parents
        p1, p2 = find(node1) , find(node2)
        
        if p1 == p2:
            return False
        
        if rank[p1] > rank[p2]:
            parent[p2] = p1
            rank[p1] += rank[p2]
            
        else:
            parent[p1] = p2
            rank[p2] += rank[p1]
            
        return True
        
    
    for n1, n2 in edges:
        if not union(n1, n2):
            return [n1, n2]
  
  
edges = [[1, 2], [1, 3], [2, 3]]          
print(findRedundantConnection(edges))