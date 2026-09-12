# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = [] 

        if not root:
            return [] 
        
        q= deque([(root, 0)]) 
       
        level = defaultdict(list) 
        n = 0 
        while q:
            node, lvl = q.popleft() 
            level[lvl].append(node.val)
             
            if node.left:
                q.append((node.left, lvl + 1)) 
            if node.right:
                q.append((node.right, lvl + 1)) 
            
        return [level[i] for i in range(len(level))]