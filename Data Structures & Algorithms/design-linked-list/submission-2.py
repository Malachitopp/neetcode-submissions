class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 


    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1 

        current = self.head
        for _ in range(index):
            current = current.next
        return current.val
        

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if self.size == 0 : 
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node
        self.size += 1 

        


    def addAtTail(self, val: int) -> None:
        node = Node(val) 
        if self.head is None:
            self.head = node
            self.tail = node
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = node
        node.prev = current
        self.tail = node 


        self.size += 1 

        
        

    def addAtIndex(self, index: int, val: int) -> None:
        node = Node(val)
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return 


        current = self.head
        for _ in range(index-1): 
            current = current.next
        node.next = current.next 
        node.prev = current
        current.next.prev = node
        current.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        

        if index < 0 or index >= self.size:
            return
        current = self.head
        for _ in range(index):
            current = current.next

        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next

        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)