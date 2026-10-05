class Solution:
    def checkValidString(self, s: str) -> bool:
        Open = 0 
        closed = 0 
        stack = []
        for ch in s:
            if ch == '(':
                Open += 1 
                closed += 1 
            elif ch == ')':
                Open -= 1
                closed -= 1 
            elif ch == '*':
                Open += 1
                closed -= 1
            
            if Open < 0:
                return False 
            if closed < 0:
                closed = 0
           
            
        return closed == 0 