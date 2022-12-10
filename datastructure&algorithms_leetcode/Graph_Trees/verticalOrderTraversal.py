# given the root of a binary tree, return the vertical order of its nodes' value
# (i.e from top to bottom , column by column)
# if two nodes are in the same row and column , the order should be from left to right

# [9 has (row= -1, column= -1)]
# [3 has (row=0, column=0)]
# [15 has (row=0, column=-2, )]
# [20 has (row=1, -1)]
# [20 has (row=2, -2)]

import collections
from typing import Optional


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.root = None

    def print_queue(self):
        temp = self.root
        while temp is not None:
            print(temp.value)
            temp = temp.next


class Solution: 

    def verticalOrder(self, root: TreeNode):
        if not root:
            return []

        columns_items = collections.defaultdict(list)

        # level order traversal
        queue = collections.deque([(0, root)])

        res = []
        min_column_x = float("inf")
        max_column_x = float("inf")

        while queue:
            x, node = queue.popleft()

            columns_items[x].append(node.value)

            min_column_x = min(min_column_x, x)
            max_column_x = max(max_column_x, x)

            if node.left:
                queue.append((x-1), node.left)

            if node.right:
                queue.append((x+1), node.right)


        for level in range(min_column_x, max_column_x + 1):
            res.append(columns_items[level])

        return res 


root = [3, 9, 20, None, None, 15, 7]
tr = Solution()

tr.print_queue()