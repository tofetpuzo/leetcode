# given the head of a linkedlist, return the list after sorting it in ascending order.
# head = [4, 2, 1, 3] output = [1, 2, 3, 4]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head: ListNode):
    if not head or not head.next:
        return head


    # split the linkedlist into half
    left = head
    right = getMiddleNode(head)
    tmp = right.next
    right.next = None
    right = tmp

    left = sortList(left)
    right = sortList(right)
    return mergeList(left, right)



def getMiddleNode(head):
    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def mergeList(left, right):
    tail = dummy = ListNode()
    while left and right:
        if left.val < right.val:
            tail.next = left
            left = left.next

        else:
            tail.next = right
            right = right.next#
        
        tail = tail.next

        if left:
            tail.next = left

        else:
            tail.next = right

    return dummy.next





        
    
    pass