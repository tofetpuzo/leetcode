# given the root of a binary search tree and a node p in it, return the inorder successor of that node
# in the binary search tree if the given node has no in-order successor in the tree, return null
# the successor of a node p in the node with the smallest key greater than p.val


# inoder travesal: always in sorted order

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorderSuccessorBST(root: TreeNode, p: TreeNode):
    # root = [2, 1, 3]
    successor = None
    while root:
        if p.value >= root.value:
            root = root.right
        else:
            successor = root
            root = root.left
    
    return successor