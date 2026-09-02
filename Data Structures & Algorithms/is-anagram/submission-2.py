class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = {} 
        store2 = {} 
        for ch in s:
            store[ch] = store.get(ch,0)+1
        
        for ch in t:
            store2[ch] = store2.get(ch,0) + 1 
        
        return store == store2 