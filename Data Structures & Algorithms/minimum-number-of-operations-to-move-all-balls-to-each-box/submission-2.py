class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * (  len(boxes))
        moves, balls = 0,0 

        for i in range(len(boxes)):
            res[i] = moves + balls
            moves = moves + balls 
            balls +=int(boxes[i]) 
        moves, balls = 0,0
        for i in reversed(range(len(boxes))):
            res[i] += moves + balls 
            moves = moves + balls 
            balls += int(boxes[i])
        
        return res 