class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [] 
        
        for num in range(n+1):
            count = 0 
            for i in range(32):
                count += (num >> i) & 1
            output.append(count) 

        return output                 
        