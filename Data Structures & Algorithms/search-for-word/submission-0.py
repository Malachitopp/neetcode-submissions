class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        start = word[0] 

        ROWS, COLS = len(board), len(board[0]) 

        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        visited = set() 
        def dfs(r,c, index ): 
            if index == len(word):
                return True 
            
            if (r<0 or c<0 or r>=ROWS or c>=COLS or word[index] != board[r][c] or (r,c) in visited):
                return False 
            visited.add((r,c)) 

            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if dfs(nr,nc, index + 1):
                    return True 
            visited.remove((r,c)) 
            
            return False 
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True  
        
        return False 
        



            

            

             