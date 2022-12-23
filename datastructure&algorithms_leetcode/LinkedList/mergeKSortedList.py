class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKSortedList(lists: list[list[ListNode]]):
    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        mergeLists = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if (i+1) < len(lists) else None
            mergeLists.append(mergeList(l1, l2))
        lists = mergeLists
    return lists[0]
    

def mergeList(l1: ListNode, l2: ListNode):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

        if l2:
            tail.next = l1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

        if l2:
            tail.next = l2
            
    return dummy.next

    