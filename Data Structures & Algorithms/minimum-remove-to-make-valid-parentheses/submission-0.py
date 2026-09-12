class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0 
        output = [] 

        for ch in s:
            if ch == "(":
                output.append(ch )
                count += 1 
            
            elif ch == ")" and count > 0:
                output.append(ch) 
                count -= 1 
            elif ch != ")":
                output.append(ch)  
        filtered = [] 
        for ch in output[::-1]:
            if ch == "(" and count > 0:
                count -= 1 
            else:
                filtered.append(ch) 
        return "".join(filtered[::-1]) 
                
                
            
        
