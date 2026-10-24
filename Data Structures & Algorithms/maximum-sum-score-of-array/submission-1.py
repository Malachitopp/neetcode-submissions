class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        output = [] 
        total = sum(nums) 
        prefix = 0 
        for i in range(len(nums)):
            prefix += nums[i] 
            suffix = total - prefix + nums[i]
            output.append(max(prefix, suffix)       )


        return max(output)
