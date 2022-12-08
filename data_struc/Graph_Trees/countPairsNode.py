# you are given the root of a binary tree and an integer distance, a pair of two different
# nodes of a binary tree is said to be good if the length of the shortest path between them
# is less than or equal to distance. return the number of good leaf node pairs in the tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# root= [1, 2, 3, None, 4] 
# distane = 3
# root = [1, 2, 3, 4, 5, 6, 7]
# distance = 3
def countPairsNode(root: 'TreeNode', distance: int):
    if not root:
        return 0

    good_pairs = 0

    def postOrder(node, distance):
        # there is no node to a leaf node to process
        if not node:
            return []

        if not node.left and not root.right:
            return [1]

        l_left_dists = postOrder(node.left, distance)
        r_right_dists = postOrder(node.right, distance)

        for l_dist in l_left_dists:
            if l_dist >= distance:
                continue

            for r_dist in r_right_dists:
                good_pairs += 1 if l_dist + r_dist <= distance else 0
        
        return [1 + dist for dist in l_left_dists + r_right_dists]
    postOrder(root, distance)

    pass