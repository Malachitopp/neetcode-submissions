class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        output = [] 
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        seen = 0 
        def dfs(r,c):
            nonlocal seen 
            grid[r][c] = 0 
            count = 1 
            for dr,dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0:
                    continue 
                
                count += dfs(nr,nc) 
            
            return count 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    seen = max(seen,dfs(r,c))
        
        return seen 