class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = 0,0 
        output = ""
        maxlen = min(len(word1), len(word2) )
        while l1 <=maxlen-1 and  l2<= maxlen-1 :
            output += word1[l1] + word2[l2] 
            l1 += 1 
            l2 += 1 
        
        if len(word1) < len(word2):
            while l2 < len(word2):
                output += word2[l2]
                l2 += 1 
            
        if len(word1) > len(word2):
            while l1 < len(word1):
                output += word1[l1]
                l1 += 1 
        return output 