class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        bottom = [1] * n

        for c in range(m-1):
            new = [1] * n  
            for r in range(n -2, -1, -1):
                new[r] = bottom[r] + new[r+1] 
            bottom = new 
        return bottom[0] 