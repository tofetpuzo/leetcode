# given the root of a binary tree, return the most frequent subtree sum.
# if there is a tie, return all the values with the highest frequency in any order. The subtree sum of a node is defined as the sum of all
#  the node values formed by the subtree, rooted at that node(including the node itself)
import collections


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right