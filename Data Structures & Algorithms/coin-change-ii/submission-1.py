class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {} 

        def dfs(i, remaining):
            if remaining == 0:
                return 1
            if i >= len(coins) or remaining < 0:
                return 0 
            if (i,remaining) in cache:
                return cache[i,remaining]
            
            cache[(i,remaining)] = dfs(i, remaining - coins[i]) + dfs(i + 1, remaining)

            return cache[(i,remaining)]

        return dfs(0, amount)