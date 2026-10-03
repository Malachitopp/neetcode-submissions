class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0] 
        curMax=1
        curMin = 1

        for num in nums:
            temp = curMax * num 
            curMax = max(num, temp, num * curMin) 
            curMin = min(num, temp, num * curMin)
            res = max(res, curMax)

        return res 