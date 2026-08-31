class Solution:
    def reverse(self, x: int) -> int:
        neg = True if x < 0 else False
        x = abs(x)

        output = []
        if x == 0:
            return 0
        while x:
            output.append(x % 10)
            x //= 10

        answer = int("".join(map(str, output)))

        if neg:
            answer *= -1
        
        return answer if -2**31 <= answer <= 2**31 -1 else 0 
        # 1. handle the empty-output case (x was 0)
        # 2. answer = the join line I gave you
        # 3. if neg, negate it
        # 4. return 0 if outside -2**31 .. 2**31 - 1, else answer