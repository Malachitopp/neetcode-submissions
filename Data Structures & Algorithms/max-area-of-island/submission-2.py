class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) 
        maxArea = 0
      
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r,c):
            
           
            if r >= rows or c >= cols or grid[r][c] == 0  or r <0 or c < 0:
                return 0
            grid[r][c] = 0  


            count = 1 
            for dr, dc in directions:
                count += dfs(r+dr, c+dc)

            return count
            





        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea,dfs(r,c))  
        
        return maxArea
