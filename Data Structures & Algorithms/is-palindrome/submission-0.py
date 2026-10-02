import string 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        translator = str.maketrans('', '', string.punctuation)

        toCheck = s.translate(translator)
        toCheck=toCheck.lower() 
        toCheck=toCheck.replace(" ", "")
        print(toCheck)
        for i, letter in enumerate(reversed(toCheck)):
            if letter != toCheck[i]:
                return False 
        return True 