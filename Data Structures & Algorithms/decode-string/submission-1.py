class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] 
        i = 0
        
        integers = set("0123456789")
        for ch in s:
            
            if ch == "]":
                mult = ""
                factor = ""
                while stack and stack[-1] != "[":
                    mult = stack.pop() +mult 
                stack.pop() 
                while stack and stack[-1] in integers:
                    factor = stack.pop() + factor
                stack.append(int(factor) * mult)

            else:
                stack.append(ch) 
            

        
        return "".join(stack)