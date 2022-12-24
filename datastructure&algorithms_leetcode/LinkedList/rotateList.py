# 61. Rotate List
# Medium

# Companies

# Given the head of a linked list, rotate the list to the right by k places.
# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateList(head: ListNode, k: int):
    if not head:
        return head
    
    # get the length of the linklist
    length, tail = 1, head
    while tail.next:
        tail = tail.next
        length+=1
    
    # this is for rotating
    k = k % length
    if k == 0:
        return head

    # move to the pivot and rotate
    cur = head
    for i in range(length - k -1):
        cur = cur.next

    newHead = cur.next
    cur.next = None
    tail.next = head

    return newHead

