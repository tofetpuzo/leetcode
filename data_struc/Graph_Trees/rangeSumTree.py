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
    pass