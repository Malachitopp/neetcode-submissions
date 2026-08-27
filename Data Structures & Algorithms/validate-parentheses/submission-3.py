class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        closed = {"}":"{", ")": "(", "]":"["}

        for ch in s:
            if ch in closed:
                if stack and stack[-1] == closed[ch]:
                    stack.pop() 
                else:
                    return False 
            else:
                stack.append(ch) 
        
        return not stack 