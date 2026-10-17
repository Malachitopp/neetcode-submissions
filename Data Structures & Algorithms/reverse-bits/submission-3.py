class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 
        for i in range(32):
            isItOne = (n >> i) & 1 
            res += (isItOne << 31 - i ) 

        return res