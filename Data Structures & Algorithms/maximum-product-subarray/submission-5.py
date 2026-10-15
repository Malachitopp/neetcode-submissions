class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0] 
        currMax, currMin = 1, 1

        for num in nums:
            temp = currMax * num 
            currMax = max(num, temp, currMin * num) 
            currMin = min(num, temp, currMin * num )
            res = max(currMax, res) 
        return res