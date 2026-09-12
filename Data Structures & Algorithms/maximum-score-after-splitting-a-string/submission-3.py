class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s) 

        prefix = [0] * n 
        postfix = [0] * n 

        if s[0] == "0":
            prefix[0] += 1 
        
        for i in range(1, n):
            prefix[i] = prefix[i-1]
            if s[i] == "0":
                prefix[i] += 1 
            
        
        if s[-1] == "1":
            postfix[-1] += 1 
        
        for i in range(n-2, -1, -1):
            postfix[i] = postfix[i+1] 
            if s[i] == "1":
                postfix[i] += 1 
        count = 0 
        for i in range(n-1):
            count = max(count, prefix[i] + postfix[i+1])
        
        return count 