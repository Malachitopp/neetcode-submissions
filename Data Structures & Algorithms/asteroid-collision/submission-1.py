class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] 

        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                diff = asteroid + stack[-1] 
                if diff < 0: #if asteroid larger 
                    stack.pop() 
                elif diff>0:# if asteroid destroyed 
                    asteroid = 0
                else: #if they are the same 
                    asteroid = 0 
                    stack.pop() 
            if asteroid:
                stack.append(asteroid)
        return stack
            