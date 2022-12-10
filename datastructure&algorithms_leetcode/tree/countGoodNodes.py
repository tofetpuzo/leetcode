
class TreeNode:
    def __init__(self, value=0, left= None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right
        

def countGoodNodes(root: TreeNode) -> int:
    def dfs(node, maxVal):
        if not node:
            return 0
        
        res = 1 if node.value >= maxVal else 0
        maxVal = max(maxVal, node.value)
        
        res+=dfs(node.left, maxVal)
        res+=dfs(node.right, maxVal)
        
        return res
    
    return dfs(root, root.value)
root = [3, 1, 4, 3, None, 1, 5]
css = TreeNode(root)

print(countGoodNodes(css))