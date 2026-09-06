# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val] 
        
        def dfs(node):
           
            if not node:
                return 0
            

            right = dfs(node.right)
            left = dfs(node.left)
            left = max(left, 0)
            right = max(right, 0 )
            res[0] = max(res[0],node.val + left + right) # max of splitting the tree 

            return node.val + max(left,right) # return the value of the node + either max of left or right path
        
        dfs(root)
        return res[0]
        
   