class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        bottom = [1] * n  

        for r in range(m-1):
            newRow = [1] * n
            for c in range(n -2, -1, -1 ):
                newRow[c] = bottom[c] + newRow[c+1]
            bottom = newRow
        return bottom[0] 
                
                