class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            number = (n >> i ) & 1 
            if number == 1:
                count += 1
        
        return count 
