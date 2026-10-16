class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
    
        rows, cols = len(board), len(board[0])
        q = deque() 
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or
                        c == 0 or c == cols - 1) and board[r][c] == "O":
                        board[r][c] = 'S'
                        q.append((r, c))

        while q:
            r, c = q.popleft() 
            
            for dr, dc in directions:
                nr, nc = dr + r, dc + c 
                if nr<0 or nc<0 or nc>=cols or nr>=rows or board[nr][nc] != 'O':
                    continue 
                board[nr][nc] = 'S'
                q.append((nr,nc)) 

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] =='S':
                    board[r][c] = 'O'
        