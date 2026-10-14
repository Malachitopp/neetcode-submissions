class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(i, current):
            if current == amount:                       # check success first
                return 0
            if current > amount or i >= len(coins):     # overshot, or no coins left
                return float('inf')
            if (i, current) in cache:
                return cache[(i, current)]

            cache[(i, current)] = min(
                1 + dfs(i, current + coins[i]),   # use coin i (and allow using it again)
                dfs(i + 1, current)               # stop using coin i, move on
            )
            return cache[(i, current)]

        res = dfs(0, 0)
        return res if res != float('inf') else -1