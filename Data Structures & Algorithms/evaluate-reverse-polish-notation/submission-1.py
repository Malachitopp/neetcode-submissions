import operator 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a,b : int(a/b) 
        }

        for val in tokens:
            if val in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[val](a, b))
            else:
                stack.append(int(val))
        return stack[-1]
            

