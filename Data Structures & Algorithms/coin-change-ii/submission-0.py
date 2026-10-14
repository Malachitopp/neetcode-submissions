class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {} 

        def dfs(i, remaining):
            if remaining == 0:
                return 1 
            if remaining < 0 or i == len(coins):
                return 0 
            if (i, remaining) in cache:
                return cache[(i, remaining)] 
            
            ways = dfs(i, remaining - coins[i]) + dfs(i + 1, remaining)

            cache[(i, remaining)] = ways 
            return cache[(i, remaining)] 

        return dfs(0, amount)
     