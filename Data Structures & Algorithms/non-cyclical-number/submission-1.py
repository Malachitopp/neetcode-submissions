class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set() 
        def dfs(n):
            number = str(n) 
            res = 0 
            if n ==1:
                return True 
            if n in visited:
                return False
            visited.add(n) 
            for num in number:
                res += int(num) **2 
            return dfs(res) 
        
        return dfs(n) 