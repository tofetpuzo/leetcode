# given the root of a binary tree, return the level order traversal of its nodes' values (i.e from left to right, level by level)
import collections


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(root: TreeNode):
        if not root:
            return []
        res = []
        queue = collections.deque([root])
        
        while queue:
            level_items = []
            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.value)
                    
                if node.right:
                    queue.append(node.value)
                    
            res.append(level_items)
                    
            return res
        
root = [3, 9, 20, None, 15, 7]   
cd = TreeNode(root)
clss = Solution()

print(clss.levelOrder(cd))
                               
