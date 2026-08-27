class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output = [] 
        output += self.inorderTraversal(root.left)
        output.append(root.val)
        output += self.inorderTraversal(root.right)
        return output