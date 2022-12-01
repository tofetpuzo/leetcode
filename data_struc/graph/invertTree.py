class TreeNode:
    def __init__(self, value=0, left= None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right
        
def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    
    # swap the children
    temp = root.left
    root.left = root.right
    root.right = temp
    
    invertTree(root.left)
    invertTree(root.right)
    
    return root