class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        row, col = len(grid), len(grid[0])
        fresh = 0 
        q = deque() 
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1 
                if grid[r][c] == 2:
                    q.append((r,c)) 
        time = 0 
        while q and fresh:
            for adj in range(len(q)):
                r, c = q.popleft() 
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc 
                    if nr<0 or nc<0 or nr >=row or nc >= col or grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue 
                    fresh -= 1 
                    grid[nr][nc] = 2
                    
                    q.append((nr,nc))
            time += 1 
        return time if fresh == 0 else -1