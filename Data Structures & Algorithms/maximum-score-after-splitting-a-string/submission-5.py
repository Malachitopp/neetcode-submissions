class Solution:
    def maxScore(self, s: str) -> int:
        prefix = [0] * len(s) 
        postfix = [0] * len(s) 

        if s[0] == '0':
            prefix[0] += 1

        for i in range(1,len(s)):
            prefix[i] = prefix[i-1]
            if s[i] == '0':
                prefix[i] += 1 
            
        
        if s[-1] == '1':
            postfix[-1] += 1 
        
        for i in range(len(s) - 2, - 1, -1):
            postfix[i] = postfix[i+1]
            if s[i] == '1' :
                postfix[i]  +=1 
            
        count = 0 
        for i in range(len(s)-1):
            count = max(count, prefix[i] + postfix[i+1])
        return count