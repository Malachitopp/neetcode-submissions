class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        running = 0

        for n in nums:
            if running < 0:
                running = 0 
            running += n 
            maxSum = max(maxSum, running) 
        return maxSum 