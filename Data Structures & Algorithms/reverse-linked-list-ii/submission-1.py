# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = left
     
        dummy = ListNode(0, head) 
        leftprev = dummy 

        for i in range(left -1):
            leftprev = leftprev.next 
        
        curr = leftprev.next 

        prev = None 
        original = curr 

        
        while count <= right:
            nxt = curr.next 
            curr.next = prev
            prev = curr
            curr = nxt 
            count += 1
        
        leftprev.next = prev 
        original.next = curr

        return dummy.next 
        
        
             
