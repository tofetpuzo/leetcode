# 92. Reverse Linked List II
# Medium
# 8.4K
# 377
# Companies

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Example 1:

# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(self, head, left: int, right: int):
    dummy = ListNode(0, head)

    leftPrev, curr = dummy, head
    for i in range(left - 1):
        leftPrev, curr = curr, curr.next
    
    # now cur ="Left", leftPrev="node before left"
    # 2) reverse from left to right
    prev = None
    for i in range(right - left +1):
        tmp = curr.next
        curr.next = prev
        prev , curr = curr, tmp
    

    # 3) update pointers
    leftPrev.next.next = curr #curr is node after "right"
    leftPrev.next = prev #prev is "right"

    return dummy.next



