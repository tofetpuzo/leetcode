# given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range [low, high]
# root = [10, 5, 15, 3, 7, None, 18], low = 7 and , high = 15
# output = 32, explanation Nodes 7, 10, 15 are in the range [7, 15], 7 + 10 + 15 = 32

from typing import Optional


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def rangeSumBST(root: Optional[TreeNode], low: int, high: int):

    range_sum = 0

    dfs(root, low, high)

       # recursively

    def dfs(node, low, high):
        if not node:
            return None

        if node:
            if low<= node.value <= high:
                ans+= node.value

            if low < node.value:
                dfs(node, low, high)

            if node.value < high:
               dfs(node, low, high)

    return range_sum

    if not root:
        return None

    ans = 0
    stack = [root]

    # iteratively

    while stack:
        node = stack.pop()
        
        if node:
            if low <= node.value <= high:
                ans+= node.value

            if low < node.value:
                stack.append(node.left)
            
            if node.value < high:
                stack.append(node.right)

    return ans

 


            