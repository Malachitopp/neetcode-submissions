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
        def dfs(a, visited, current):
            visited.add(a) 
            nonlocal count 
            if m <= current <= n:
                count += 1 
            
            if current >= n:
                return 

            for nextDot in range(1,10):
                if nextDot in visited:
                    continue
                skip_dot = skip.get((a, nextDot), 0)
                if skip_dot != 0 and skip_dot not in visited:
                    continue  # illegal move — skip this candidate
                    
                visited.add(nextDot) 
                dfs(nextDot, visited, current+1)
                visited.remove(nextDot) 
            
        
        for i in range(1,10):
            dfs(i, set(), 1)
        
        return count 
                

            
                