# given the root of a binary tree and an array of treenode objects nodes, return LCA OF ALL THE NODES IN nodes. 
# All the Nodes will exist in the tree and all values  of the tree's node are unique
# example nodes = [7, 6, 2, 4] return 6 -> 3->5, 1


from typing import List


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def lowestCommonAncestor(root: 'TreeNode', nodes: 'List[TreeNode]'):
    nodes = set(nodes)

    def dfs(node):
        if not node:
            return None

        if node in nodes:
            return node
        
        l = lowestCommonAncestor(root.left)
        r = lowestCommonAncestor(root.right)

        if l and r:
            return root

        else:
            return l or r

    return dfs(root)