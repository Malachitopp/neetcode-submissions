class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = set() 
        
        def dfs(n):
            string = str(n) 
            res = 0 
            if n in cycle:
                return False
            if n == 1:
                return True
            for num in string:
                res += int(num)**2 
            cycle.add(n) 
            return dfs(res) 
            
            
        return dfs(n) 