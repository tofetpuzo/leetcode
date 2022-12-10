# Given a binary tree root, a node X in the tree is named good, if in the path from root to X
# there are no nodes with a value greater than X, return the number of good nodes in the binary tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def goodNodes(root: TreeNode, ):
    if not root:
        return 0
    good_nodes = 0
    
    
    
    def dfs(node, max_seen):
        if not node:
            return
        
        if root.value >= max_seen:
            good_nodes +=1
            
            max_seen = max(max_seen, node.value)
        
        dfs(root.left, max_seen)
        dfs(root.right, max_seen)
            
        
        
    dfs(root, 10001)
    return good_nodes    
        