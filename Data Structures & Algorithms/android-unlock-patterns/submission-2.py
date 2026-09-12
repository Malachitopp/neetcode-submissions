class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = {
            (1,3): 2, (3,1): 2,
            (1,7): 4, (7,1): 4,
            (3,9): 6, (9,3): 6,
            (7,9): 8, (9,7): 8,
            (1,9): 5, (9,1): 5,
            (3,7): 5, (7,3): 5,
            (4,6):5, (6,4):5,
            (2,8):5,(8,2):5,
        }

        count = 0 

        def dfs(now, current, visited):
            nonlocal count 

            
            
            if m<= current <= n:
                count += 1 
            
            visited.add(now) 

            

            for i in range(1,10):
                if i in visited:
                    continue 
                skipnumber = skip.get((now,i), 0)
                if skipnumber != 0  and skipnumber not in visited:
                    continue 
                visited.add(i)
                dfs(i, current + 1, visited) 
                visited.remove(i) 
            
        for i in range(1,10):
            dfs(i, 1, set()) 
        return count 


