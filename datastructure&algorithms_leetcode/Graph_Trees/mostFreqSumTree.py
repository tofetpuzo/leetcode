# given the root of a binary tree, return the most frequent subtree sum.
# if there is a tie, return all the values with the highest frequency in any order. The subtree sum of a node is defined as the sum of all
#  the node values formed by the subtree, rooted at that node(including the node itself)
import collections


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findFrequentTree(root: TreeNode):
    if not root:
        return []

    # freq_dict stores numbers hence why i incremented it.

    freq_dict = collections.defaultdict(int)
    max_freq = 0

    dfs(root)
    res = []

    for val, freq in freq_dict.items():
        if freq == max_freq:
            res.append(val)

    def dfs(node):
        if not node:
            return 0

        if not node.left and not node.right:
            freq_dict[node.value] += 1

            max_freq = max(max_freq, freq_dict[node.value])

            return node.value

        l_sum = dfs(node.left)
        r_sum = dfs(node.right)

        cur_sum = node.value + l_sum + r_sum
        
        freq_dict[cur_sum] +=1
        max_freq =max(max_freq, cur_sum)
        
        return cur_sum
