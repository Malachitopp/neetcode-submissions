class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 
        for i in range(32):
            #move position i to position 0 and then check if its 0 or 1
            bit = (n >> i) & 1 
            # move the bit to position 31 - i to swap it 
            res +=  (bit << (31 - i))
        return res 