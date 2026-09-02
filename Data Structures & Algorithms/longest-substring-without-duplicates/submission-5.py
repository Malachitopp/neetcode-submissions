class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0 
        store = {} 
        maxLength = 0 

        while r <= len(s)-1:
            
            if s[r] in store: 
                l = store[s[r]] + 1 if l < store[s[r]] + 1 else l 
                
            store[s[r]] = r
            maxLength = max(maxLength, r-l+1) 
            r += 1

        return maxLength