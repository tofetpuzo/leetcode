# you are given two non-empty linked lists representing two non-negative integers
# The digits are stored in reverse order and each of their nodes contains a 
# single digit. add the two numbers and return a linked list
# you may assume the two number do not contain any leading zero except the number 0 itself

# (2 -> 4 -> 3) +  (5 -> 6 -> 4) -> 807

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def addTwoNumbers(l1: ListNode, l2: ListNode):
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.value if l1 else 0
            v2 = l2.value if l2 else 0

            # calculate the new digits
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
