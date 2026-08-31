class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        output = []
        for i in range(len(boxes)):
            iters = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    iters+= abs(i-j) 
            output.append(iters)
        return output 
        
