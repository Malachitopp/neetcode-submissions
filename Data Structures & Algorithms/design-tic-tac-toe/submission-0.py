class TicTacToe:

    def __init__(self, n: int):
        self.n = n 
        self.row = [0] * n 
        self.column = [0] * n
        self.diagonal = 0 
        self.antiDiagonal = 0 

    def move(self, row: int, col: int, player: int) -> int:
        current = 1 if player == 1 else -1 

        self.row[row] += current
        self.column[col] += current

        if row == col: 
            self.diagonal += current 
        if col == (len(self.column) - row - 1):
            self.antiDiagonal += current 
        
        n = len(self.row) 

        if (abs(self.row[row]) == n or
            abs(self.column[col]) == n or
            abs(self.diagonal) == n or
            abs(self.antiDiagonal) == n):
            return player
        return 0 



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
