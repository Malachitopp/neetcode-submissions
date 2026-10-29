# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 
        start = head.next 
        right = start
        left = head 
        while right and right.next :
            nxt = right.next.next
            nxt_left = left.next.next 

            left.next = left.next.next 
            right.next = right.next.next
            right = nxt 
            left = nxt_left 
        #This should make right a list of every second node 
        left.next = None 

        left, right = head, start 
        while right:
            nxtL, nxtR= left.next, right.next 
            
            right.next = left 
            left.next = nxtR if nxtR else nxtL 
            left, right = nxtL, nxtR

        return start
        
