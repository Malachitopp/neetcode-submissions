class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0 
        r, l = 0, 0 

        while r < len(prices):
            if prices[l] < prices[r]:
                maxP = max(maxP, prices[r] - prices[l])
            # if the day you bought on l, has a price[l] more expensive than tomorrows price price[r] then you want to move to tomorrow
            else:
                l = r 
            r +=  1
        return maxP