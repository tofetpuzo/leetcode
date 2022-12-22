class LinkedList:
    def __init__(self, value):
        self.value = value
        self.head = None
        self.next = None


    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return '->'.join(values)

    
class Solution:
    def reOrderList(self, head: LinkedList):
        slow , fast = head, head.next
        # the aim of this code is to find the middle of the list.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1 , tmp2
        
