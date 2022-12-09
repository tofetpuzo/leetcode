class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p:'TreeNode', q:'TreeNode' ):
        self.p_found = False
        self.q_found = False

        ans = self.dfs(root, p, q)
        return ans if self.p_found and self.q_found else None

    def dfs(self, node, p, q):
        if not node:
            return None
        # post order tranersal
        l = self.dfs(node.left, p, q)
        r = self.dfs(node.right, p, q)
        
        if p == node or q == node:
            if p == node:
                self.p_found = True
            else:

                self.q_found = True
            return node
        

        if l and r:
            return node
            
        else:
            return l or r
        