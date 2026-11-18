class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        block = 2**(n - 1) 
        
        output = [] 

        if k > 3 * block:
            return "" 
        
        index = k -1 


        for i in range(n):
            candidates = [c for c in 'abc' if not output or c != output[-1]]
            output.append(candidates[index // block] ) 
            index %= block 
            block //= 2 

        
        return "".join(output)

