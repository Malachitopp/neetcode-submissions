class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        cur = [] 

        def dfs(openN, closedN):
            if openN == closedN == n:
                string = "".join(cur.copy())
                output.append(string) 
                return 
            if openN < n:
                cur.append('(')
                dfs(openN + 1, closedN)
                cur.pop() 
            if closedN < openN:
                cur.append(')')
                dfs(openN, closedN +1)
                cur.pop() 
        dfs(0,0)
        return output 