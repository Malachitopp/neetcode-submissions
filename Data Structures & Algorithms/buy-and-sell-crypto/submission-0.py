class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0] 
        best = 0 
    
        for price in prices:
            # if i sold today, the best profit is the price today minus the lowest price vs the best seen profit 
            best = max(best, price - min_price) 
            # check if the min price is smaller than the current price
            min_price = min(min_price, price) 

        return best 
