class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = target[0] 
        
        for i in range(1,len(target)):
            if target[i] > target[i-1]:
                difference = target[i] - target[i-1] 
                res += difference 
        
        return res 