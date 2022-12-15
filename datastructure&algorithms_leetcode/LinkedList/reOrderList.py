class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return '->'.join(values)


