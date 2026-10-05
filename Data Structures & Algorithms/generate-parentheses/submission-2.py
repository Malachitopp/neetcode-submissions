class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = [] 
        current = [] 
        def dfs(openN, closedN):
            if openN == closedN == n:
                output.append("".join(current)) 
                return 
            if openN < n:
                current.append('(')
                dfs(openN +1, closedN)
                current.pop() 
            if closedN < openN :
                current.append(')')
                dfs(openN, closedN +1) 
                current.pop() 

        dfs(0,0) 
        return output                 