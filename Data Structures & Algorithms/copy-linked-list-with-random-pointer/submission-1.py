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
        cur=head 
        prev={None:None}

        while cur:
            copy = Node(cur.val) 
            prev[cur] = copy 
            cur=cur.next 
        cur = head 
        while cur:
            copy = prev[cur] 
            copy.next = prev[cur.next]
            copy.random=prev[cur.random]
            cur = cur.next 
        return prev[head] 
            