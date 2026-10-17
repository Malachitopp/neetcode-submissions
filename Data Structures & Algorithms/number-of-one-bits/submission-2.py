class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0 
        for i in range(32):
            xor = (n >> i ) & 1 
            count += xor 
        return count 
