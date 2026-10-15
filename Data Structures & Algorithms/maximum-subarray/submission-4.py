class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0] 
        cur = 0 

        for num in nums:
            cur += num 
             
            maxSum = max(maxSum, cur)
            if cur < 0:
                    cur = 0
        return maxSum 