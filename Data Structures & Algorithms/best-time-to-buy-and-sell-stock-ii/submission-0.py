class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        l = 0
        r = 0
        maxP = []
        while r  < len(nums):
            if nums[l] < nums[r]:
                maxP.append(nums[r] - nums[l])
                l += 1
            else:
                l = r 
            r += 1
        return sum(maxP)


