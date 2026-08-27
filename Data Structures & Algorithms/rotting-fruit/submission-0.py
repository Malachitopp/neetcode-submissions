class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        neighbours = [[1,0],[0,1],[-1,0],[0,-1]]
        def bfs(grid):
            visited = set()
            queue = deque()
            fresh_count = 0
            for i, row in enumerate(grid):
                for j, health in enumerate(row):
                    if health == 2:
                        queue.append((i,j))
                        visited.add((i,j)) 
                    elif health == 1:
                        fresh_count += 1
            if fresh_count == 0:
                return 0
            minute = -1
            while queue:
                for i in range(len(queue)):
                    r,c = queue.popleft() 
                    for dr, dc in neighbours:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc] == 1:
                            fresh_count -= 1
                            queue.append((nr, nc))
                            visited.add((nr, nc))
                minute += 1
            return minute if fresh_count == 0 else -1

        return bfs(grid)