# given a linked list reverse the nodes of a linked list k at a time and return the modified list
# k is a +ve integer and is less than or equal to the length of the linked list. if the number of node.js is not a multiple of k
# then left-out nodes, in the end should remain as it is
# head = [1, 2, 3, 4, 5] k =2
# output = [2, 1 , 4, 3, 5]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseNodesInKGroups(head: ListNode, k: int):
    dummy = ListNode(0, head)
    groupPrev = dummy

    while True:
        kthNode = getKthNode(groupPrev, k)
        # if kthNode is the last element
        if not kthNode:
            break

        
        # [dummy, 1, 2] ,[3 , 4]
        #  ^             ^ this is GroupNext
        groupNext = kthNode.next

        # reverse group
        prev , curr = kthNode.next, groupPrev.next
        
        while curr != groupNext:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # reversing the list
        tmp = groupPrev.next
        groupPrev.next = kthNode
        groupPrev = tmp

    return dummy.next

def getKthNode(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -=1
    return curr

