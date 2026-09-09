class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        store =  {} 
        n = len(grid)
        for row in range(n):
            for col in range(n):
                store[grid[row][col]] = store.get(grid[row][col],0) + 1
        a = 0
        b = 0 
        for num in range(1, n**2+1):
            if store.get(num,0) == 0:
                b = num 
            if store.get(num,0) == 2:
                a = num 
            
        return [a,b]
            

            
        


