class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cache = {}
        max_sum = -float('inf')

        def dfs(i):
            nonlocal max_sum
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]

            # Subarray must be contiguous, so extend or just take nums[i]
            curr = max(nums[i], nums[i] + dfs(i + 1))
            max_sum = max(max_sum, curr)
            cache[i] = curr
            return curr

        dfs(0)
        return max_sum