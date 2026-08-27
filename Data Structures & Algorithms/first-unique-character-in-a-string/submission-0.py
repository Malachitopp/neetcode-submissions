class Solution:
    def firstUniqChar(self, s: str) -> int:
        store = {} 
        for ch in s:
            store[ch] = store.get(ch, 0) + 1 

        for i, ch in enumerate(s):
            if store[ch] == 1:
                return i 
        return - 1