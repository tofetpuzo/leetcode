# given the head of a linked lost, remove the nth node from the end of the list and return its head

# head = [1, 2, 3, 4, 5], n= 2
# output = [1, 2,  3, 5]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthNode(head: ListNode, n: int):
    dummy = ListNode(0, head)

    left = dummy
    right = head 
    while n > 0 and right:
        right = right.next
        n-=1
    
    while right:
        left = left.next
        right = right.next

    # delete
    left.next = left.next.next

    return dummy.next
