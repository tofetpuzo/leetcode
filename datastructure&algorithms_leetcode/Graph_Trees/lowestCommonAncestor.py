# given a binary tree, find the lowest common ancestor of two given nodes in the tree.
# according to the definition of LCA on wikipedia: 
# "the lowest common ancestor is defined between two nodes"
# p and q as the lowest node in T that has both p and q as descendents
# (where we allow a node to be a descendant of itself)
# p = 5, q = 1 -> return 3
# p = 5, q = 4 -> return 5
# p =2 , q = 7 -> return 2


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def lowestCommonAncestor(root: 'TreeNode', p:'TreeNode', q:'TreeNode' ):
    if not root:
        return None
    
    if root == p or root ==q:
        return root
    
    l = lowestCommonAncestor(root.left, p, q)
    r = lowestCommonAncestor(root.right, p , q)

    if l and r:
        return root
    else:
        return l or r