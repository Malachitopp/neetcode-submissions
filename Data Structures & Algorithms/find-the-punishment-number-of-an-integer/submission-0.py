class Solution:
    def punishmentNumber(self, n: int) -> int:
        valid_numbers = [] 

        squares = [i * i for i in range(1,n+1)]

        
        def dfs(i, target, current, digits):
            if i == len(digits):
                return sum(current) == target
            
            for j in range(i + 1, len(digits) + 1):
                current.append(int(digits[i:j]))
                if dfs(j, target, current, digits):
                    return True 
                current.pop() 
            return False

        for root, square in enumerate(squares, start=1):
            if dfs(0, root, [], str(square)):
                valid_numbers.append(root)

        return sum(c ** 2 for c in valid_numbers)

        
