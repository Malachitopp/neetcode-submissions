"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        prev = {None: None}
        curr = head
        
        while curr:
            copy = Node(curr.val) 
            prev[curr] = copy 
            curr = curr.next 
        
        curr = head 
        while curr: 
            copy = prev[curr] 
            copy.next = prev[curr.next]
            copy.random = prev[curr.random]
            curr = curr.next 

        return prev[head]