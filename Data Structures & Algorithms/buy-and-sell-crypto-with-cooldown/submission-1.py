class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache= {} 

        def dfs(i, buying):
            if i >= len(prices):
                return 0 
            if (i, buying) in cache:
                return cache[(i,buying)]

            if buying:
                cache[(i,buying)] = max(dfs(i+1, True), -prices[i] + dfs(i+1, False))
            else:
                cache[(i,buying)] = max(dfs(i+1, False), prices[i] + dfs(i+2, True))
            return cache[(i,buying)]

        return dfs(0,True)