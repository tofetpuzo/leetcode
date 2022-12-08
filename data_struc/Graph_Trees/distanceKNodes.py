# given the root of a binary tree, the value of a target node target, an integer k, return an array of the
# values of all nodes that have a distance k from the target node.
# target = 5
# k = 2
# output = [7, 4, 1]
# convert tree to a graph where each of the vertice can be considered to be a tree
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def distanceKNodes(root: TreeNode, target: TreeNode, distance: int):
    # first step: represent the nodes as a graph
    # each key will be the node

    if not distance:
        return [target.value] 
    
    graph = defaultdict(list)
    
    queue = deque([root])
    
    
    while queue:
        node = queue.popleft()
        if node.left:
            graph[node].append(node.left)
            graph[node.left].append(node)
            queue.append(node.left)

        if node.right:
            graph[node].append(node.right)
            graph[node.right].append(node)
            queue.append(node.right)


    res = []
    visit = set([target])
    # 0 in queue stands for k
    queue =  deque([(target, 0)])
    while queue:
        node, dist = queue.popleft()

        if dist == distance:
            res.append(node)
        else:
            for edge in graph[node]:
                if edge not in visit:
                    visit.add(edge)
                    queue.append((edge, dist+1))

    return res
