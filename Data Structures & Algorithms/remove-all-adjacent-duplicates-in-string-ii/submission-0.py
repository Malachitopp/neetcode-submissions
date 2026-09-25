class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        
       
        for letter in s:
            stack.append(letter)
            count = 0 
            if len(stack)>=k:
                if len(set(stack[-k:])) == 1:
                    for _ in range(k):
                        stack.pop() 
        
        return "".join(stack) 
    

                        