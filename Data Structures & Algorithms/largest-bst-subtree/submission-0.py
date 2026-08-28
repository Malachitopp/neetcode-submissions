# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.best = 0 

        def dfs(node):
            if not node:
                return (True, float("inf"), float("-inf"), 0)

            l_bst, l_min, l_max, l_size = dfs(node.left)
            r_bst, r_min, r_max, r_size = dfs(node.right)

            if l_max < node.val and r_min > node.val and l_bst and r_bst:
                size = l_size + r_size + 1
                self.best = max(self.best, size) 
                return (True, min(l_min, node.val), max(r_max, node.val), size) 
            return (False, 0 , 0 , 0) 
        
        dfs(root) 
        return self.best 