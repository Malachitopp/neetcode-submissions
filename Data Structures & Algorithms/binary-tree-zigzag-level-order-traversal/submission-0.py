# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [] 

        q= deque([(root, 0)]) 
        level = defaultdict(list)
        while q: 
            node, lvl = q.popleft() 
            level[lvl].append(node.val)
            
            if node.left:
                q.append((node.left, lvl + 1))
            if node.right:
                q.append((node.right, lvl + 1)) 
    
        return [level[i][::-1] if i % 2 != 0 else level[i] for i in range(len(level))]
