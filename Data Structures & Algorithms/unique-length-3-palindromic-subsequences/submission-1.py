class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        output = 0 

        for ch in "abcdefghijklmnopqrstuvwxyz":
            first = s.find(ch) 
            last = s.rfind(ch) 
            if first == -1:
                continue 
            output += len(set(s[first+1:last])) 
        
        return output 
                

        