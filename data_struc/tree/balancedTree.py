
class TreeNode:
    def __init__(self, value=0, left= None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right
        

def balancedTree(root: TreeNode) -> bool:
    def dfs(root):
        if not root : return [True , 0]
        
        left, right = dfs(root.left) , dfs(root.right)
        balanced =(left[0] and right[0] and abs(left[1] - right[1]) <= 1)
        
        return [balanced, 1 + max(left[1], right[1])]
        
    return dfs(root)[0]


root = [3, 9 , 20, None, None,  15, 7]
css = TreeNode(root)


print(balancedTree(css))