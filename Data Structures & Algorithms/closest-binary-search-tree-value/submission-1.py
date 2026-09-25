# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = {}
        maxDiff = float("inf")

        def dfs(node):
            if not node:
                return  0 
            nonlocal maxDiff,res
            diff = abs(node.val - target)
            maxDiff= min(maxDiff,diff ) 
            res[diff] = node.val 
            dfs(node.left) 
            dfs(node.right) 
            
            return maxDiff 
        dfs(root)
        return res[maxDiff]

            