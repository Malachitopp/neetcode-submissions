class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = {(ROWS - 1, COLS - 1): 1 }
        
        def dfs(r,c):
            if r == ROWS or c == COLS  or grid[r][c] == 1 :
                return 0 
            if (r,c) in dp:
                return dp[(r,c)] 
            
            dp[(r,c)] = dfs(r +1 , c) + dfs(r, c+ 1 ) 
            return dp[(r,c)]

        return    dfs(0,0)
    







