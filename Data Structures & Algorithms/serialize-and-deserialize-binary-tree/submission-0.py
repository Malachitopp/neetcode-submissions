# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"
        
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + "," + left +","+ right
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data_split = data.split(",")
        q = deque(data_split) 
        def build(queue):
           
            c= queue.popleft() 
            if c == "#":
                return None
            node = TreeNode(int(c)) 
            node.left = build(queue)
            node.right = build(queue) 
            return node
        return build(q)


            
