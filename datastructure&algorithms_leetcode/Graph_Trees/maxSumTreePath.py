# a path in a binary tree is a sequence of nodes where each pair of adjacent nodes
# in the sequence has an edge connecting them. A node can only appear in the sequence at most once
# note that the path does not need to pass through the root.
# the path sum of a path is the sum of the node's values in the path.
# given the root of a binary tree, return the maximum path sum of any non-empty path.

from typing import Optional


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class Solution:    
    def maxSumTreePath(self, root: Optional[TreeNode]):
        
        if not root:
            return 0
    
        self.max_path_sum = root.value
        
        self.dfs(root)
        
        return self.max_path_sum
    
    def dfs(self, node):
        if not node:
            return 0
        
        # this means the node is a leaf
        if not node.left and not node.right:
            self.max_path_sum = max(self.max_path_sum, node.value)
            return node.value
        
        # post-order traversal
        l_path_sum = self.dfs(node.left)
        r_path_sum = self.dfs(node.right)
        
        self.max_path_sum = max(
            self.max_path_sum,
            node.value,
            node.value + l_path_sum + r_path_sum,
            node.value + l_path_sum,
            node.value + r_path_sum
        )
        
        return max (
            node.value,
            node.value + l_path_sum,
            node.value + r_path_sum,
            0
        )
            
            
            
        
        
    