class Solution:
    def hammingWeight(self, n: int) -> int:
        output = 0 
        for i in range(32):
            bit = (n >> i) & 1
            if bit == 1:
                output += 1
        return output 