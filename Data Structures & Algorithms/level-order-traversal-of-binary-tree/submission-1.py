# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root]) 

        output = [] 
        if not root:
            return [] 

        while q:
            level = [] 
            
            for i in range(len(q)):
                node = q.popleft() 
                left = node.left 
                right = node.right 

                level.append(node.val) 
                if left:
                    q.append(node.left) 
                if right:
                    q.append(node.right)
            output.append(level)
        return output 
