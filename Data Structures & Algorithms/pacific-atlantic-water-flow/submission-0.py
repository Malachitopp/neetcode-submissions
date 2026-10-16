class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        directions=[[1,0],[-1,0],[0,-1],[0,1]]
       
     
        pac, atl = set(), set() 

        def dfs(r,c, visited):
            visited.add((r,c))
        
            for dr, dc in directions:
                nr, nc = dr + r, dc + c 
                if nr < 0 or nc < 0 or nr >= rows or nc >=cols or (nr,nc) in visited or heights[nr][nc] < heights[r][c]:
                    continue 
                dfs(nr,nc, visited)

        for c in range(cols):
            dfs(0, c, pac)
            dfs(rows-1, c, atl)
        for r in range(rows):
            dfs(r, 0, pac) 
            dfs(r, cols -1, atl)
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
            
        