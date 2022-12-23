# given a linkedlist, swap every two adjacent node and return its head.
# you may not modify the values in the list's nodes. only nodes itself may change.
# head = [1, 2,3, 4]
# output = [2, 1 , 4, 3]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapNodePairs(head: ListNode):
    dummy = ListNode(0, head)
    prev , curr = dummy, head
    while curr and curr.next:
        # save ptrs
        nxtPair = curr.next.next
        second = curr.next

        # [dummy, 1, 2, 3 , 4]
        #  ^
        # reverse this pair
        second.next = curr
        curr.next = nxtPair
        prev.next = second

        # update pointers
        prev = curr
        curr = curr.next

    return dummy.next