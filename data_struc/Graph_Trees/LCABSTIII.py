# given two node of a binary tree p and q return their lowest common ancestor , each node
# will have a reference to its parent node. the def for node is below
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.parent = None

# this T: O(N)
# S: O(N)
def lowestCommonAncestor(p: Node, q: Node):
    seen = set()
    while p:
        seen.add(p)
        p = p.parent

    while q:
        if q in seen:
            return q

        q = q.parent

# T: O(1)

def lowestCommonAncestor2(p: Node, q: Node):
    p_copy = p
    q_copy = q
    
    while p_copy != q_copy:
        q_copy = q_copy if q_copy else p
        p_copy = p_copy if p_copy else q


    return p_copy