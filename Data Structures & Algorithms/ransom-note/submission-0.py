class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mag = {} 
        for letter in magazine:
            mag[letter] = mag.get(letter,0) + 1 
        
        for letter in ransomNote:
            if letter in mag:
                mag[letter] = mag.get(letter, 0) - 1 
                if mag[letter] == 0:
                    del mag[letter] 
            else:
                return False 
        return True 
        
