class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows, cols = len(board), len(board[0])
        visited = set() 
        def dfs(r,c,i):
            
            if board[r][c] != word[i]:
                return False 
            if i == len(word)-1 :
                return True
            visited.add((r,c)) 
            
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr < 0 or nc < 0 or nr >=rows or nc>=cols or (nr,nc) in visited:
                    continue 
                if dfs(nr,nc, i +1):
                    return True  
            visited.remove((r,c))
            return False 

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True 

        return False 