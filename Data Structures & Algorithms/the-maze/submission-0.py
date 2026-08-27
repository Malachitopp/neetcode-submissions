class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        ROWS, COLS = len(maze), len(maze[0]) 
        visited = set()

        def dfs(r,c):

            if (r,c) in visited:
                return False
            if (r,c) == (destination[0], destination[1]):
                return True 
                
            visited.add((r,c)) 

            for dr, dc in directions:
                nr, nc = r, c                      # ← fresh start per direction
                while (0 <= nr + dr < ROWS and 0 <= nc + dc < COLS
                    and maze[nr + dr][nc + dc] == 0):
                    nr += dr
                    nc += dc
                if dfs(nr, nc):
                    return True
            return False      

        return dfs(start[0],start[1])
