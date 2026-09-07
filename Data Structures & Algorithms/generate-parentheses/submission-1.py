class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []     
        stack = [] 
        
        def dfs(openN, closed): 
            if closed == openN == n :
                output.append( "".join(stack) ) 
                return 
            
            if openN < n:
                stack.append("(")
                dfs(openN+1, closed)
                stack.pop() 
            if closed < openN:
                stack.append(")")
                dfs(openN, closed + 1)
                stack.pop() 
            
        dfs(0,0) 
        return output 