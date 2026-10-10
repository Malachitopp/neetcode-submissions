# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = []
        
        def dfs(node, curr):
            if not node: 
                count.append(curr) 
                return 
            
            curr += 1 
            dfs(node.left, curr) 
            dfs(node.right, curr) 

        dfs(root, 0)
        return max(count)  
            