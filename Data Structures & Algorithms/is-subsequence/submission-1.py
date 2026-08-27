class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0 

        for letter in t:
            if i < len(s) and s[i] == letter:
                i += 1
            
        return i == len(s) 
