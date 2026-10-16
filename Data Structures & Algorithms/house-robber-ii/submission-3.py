class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {} 

        def dfs(i, first:bool):
            if i >=len(nums):
                return 0  
            if i == len(nums) -1  and first:
                return 0 
            
            if (i, first) in cache:
                return cache[(i,first)]
            
            cache[(i, first)] = max(dfs(i+1, first), nums[i] + dfs(i+2, first or i == 0))
            return cache[(i, first)]

        return max(dfs(0,True), dfs(0,False))