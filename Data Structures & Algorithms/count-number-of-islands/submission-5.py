class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        rows, cols = len(grid), len(grid[0]) 
        output = 0
        

        def dfs(r,c):
            grid[r][c] = '0'
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc 
                if nr < 0 or nc < 0  or nr >= rows or nc >= cols or grid[nr][nc] == '0':
                    continue 

                dfs(nr,nc)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r,c)
                    output += 1 
        return output
