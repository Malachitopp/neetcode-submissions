class Solution:
    def reverse(self, x: int) -> int:
        neg = True if x < 0 else False
        x = abs(x)
        output = [] 
        if x == 0:
            return 0 
        while x:
            carry = x % 10
            x  = x // 10 
            output.append(carry) 
            
        output = int("".join(map(str, output)))
        if neg:
            output *= -1 

        return output if -2**31 <= output <= 2**31 - 1 else 0