class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0]) 
        if grid[ROWS-1][COLS-1] != 0 or grid[0][0] != 0:
            return -1
        
        def bfs(grid):
            visit = set()
            queue = deque() 
            queue.append((0,0))
            visit.add((0,0))

            length = 1
            while queue:
                for i in range(len(queue)):
                    r,c = queue.popleft()
                    if r == ROWS - 1 and c == COLS -1:
                        return length
                    neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1,-1], [-1,1], [1,-1],[1,1]]
                    for dr, dc in neighbours:
                        if (min(r+dr, c+dc)<0 or r+dr == ROWS or c+dc==COLS or (r+dr, c+dc) in visit or grid[r+dr][c+dc] == 1):
                            continue
                        queue.append((r+dr,c+dc))
                        visit.add((r+dr,c+dc))
                length += 1 
            return -1 
        
        return bfs(grid)