# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head 
       
        count = 0 
        while cur:
            nxt = cur.next 
            cur = nxt 
            count += 1 
        
        if count % 2 == 0:
            middle = count // 2 
        else:
            middle = count // 2
        tracker = 0

        cur = head 
        while tracker != middle:
            nxt = cur.next 
            cur = nxt 
            tracker += 1
        
        
        return cur
