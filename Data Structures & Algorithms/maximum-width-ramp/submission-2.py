class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        output = 0 
        stack = [] 
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i) 

        for j in range(len(nums) -1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                output = max(output, j - stack.pop())

        return output