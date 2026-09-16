# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            newNode = Node(insertVal)
            newNode.next = newNode
         
            return newNode

        curr = head.next 
        prev = head
        while True:
            if prev.val <= insertVal <= curr.val: 
                node = Node(insertVal) 
                prev.next = node
                node.next = curr 
                return head 

            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    node = Node(insertVal)
                    prev.next = node
                    node.next = curr 
                    return head 
            prev, curr = curr, curr.next 
            if prev == head:
                break 
            
        prev.next = Node(insertVal, curr)
        return head
                