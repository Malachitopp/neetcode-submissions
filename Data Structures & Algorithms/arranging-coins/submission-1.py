class Solution:
    def arrangeCoins(self, n: int) -> int:
        number = n 
        output = 0 
        for i in range(1,n+1):
            number -= i 
            if number < 0:
                return output 
            output += 1 
        return output 