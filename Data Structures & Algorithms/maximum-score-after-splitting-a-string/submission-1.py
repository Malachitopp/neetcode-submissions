class Solution:
    def maxScore(self, s: str) -> int:
        output = []
        l, r = 0, len(s) 
        while l < len(s) - 1 and r > 1:
            left = {}
            right = {} 
            
            for num in s[:l+1]:
                left[num] = left.get(num, 0) + 1 
                
            for num in s[l+1:]:
                right[num] = right.get(num,0)+ 1 
            
            output.append(left.get("0",0) + right.get("1",0))
            l += 1
          
            
        
        return max(output)