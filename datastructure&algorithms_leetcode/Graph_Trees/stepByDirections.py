import collections
from typing import Optional


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def stepByDirections(root: Optional[TreeNode], startValue: int, destValue: int) -> str:
    graph = collections.defaultdict(list) 
    queue = collections.deque([root])
    
    while queue:
        node = queue.popleft()
        
        if node.left:
            graph[node.left.value].append((node.value, 'U'))
            graph[node.value].append((node.left.value, 'L'))
        
            queue.append(node.left)
        if node.right:
            graph[node.right.value].append((node.value, 'U'))
            graph[node.value].append((node.right.value, 'R'))
        
            queue.append(node.right)
            
    queue = collections.deque([(startValue, "")])
    visited = set()
    
    while queue:
        cur_val , cur_path = queue.popleft()
        
        if cur_val in visited:
            continue
        visited.add(cur_val)
        
        if cur_val == destValue:
            return cur_path
        
        else:
            for child, dir in graph[cur_val]:
                if child not in visited:
                    queue.append((cur_val , cur_path + dir))
        
        