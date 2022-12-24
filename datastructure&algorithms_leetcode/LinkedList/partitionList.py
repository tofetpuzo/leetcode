# given the head of a linkedlist and a value x, 
# partition it such that all nodes less than x come before nodes greater than or equal to x.
# head = [1, 4, 3, 2, 5, 2], x = 3
# output  = [1, 2, 2, 4, 3, 5]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partitionList(head: ListNode, x: int):
    left , right = ListNode(), ListNode()
    left_tail , right_tail = left, right
    while 