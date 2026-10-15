class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {} 

        for i in range(len(nums) -1, -1, -1):
            cache[i] = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    cache[i] = max(cache[i], 1 + cache[j])
        
        output = [i for i in cache.values() ]
        return max(output)