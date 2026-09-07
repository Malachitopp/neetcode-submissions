# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        output = [] 
        if not root:
            return 0 
        def dfs(node, total):
            if not node:
                return 
            if not node.left and not node.right: 
                output.append(int(total))  
                return total 
            if node.left:
                dfs(node.left, total + str(node.left.val))
            if node.right: 
                dfs(node.right, total + str(node.right.val)) 

         
            


        dfs(root, f"{root.val}") 
        return sum(output) 