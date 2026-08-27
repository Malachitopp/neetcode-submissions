class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 ={} 
        for letter in s:
            if letter not in hash1:
                hash1[letter] = 1 
            else:
                hash1[letter] += 1 
        for letter in t:
            if letter not in hash2:
                hash2[letter] = 1 
            else:
                hash2[letter] += 1
        if hash1 == hash2:
            return True
        return False