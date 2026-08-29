class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        
        q = deque() 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c)) 
        
        while q:
            r,c = q.popleft() 
            for dr,dc in directions:
                nr,nc = r + dr, c + dc 
                if nr >= ROWS or nc >= COLS or nr < 0 or nc<0 or grid[nr][nc] == -1 or grid[nr][nc] != INF:
                    continue 
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr,nc)) 
            
                

                


                

