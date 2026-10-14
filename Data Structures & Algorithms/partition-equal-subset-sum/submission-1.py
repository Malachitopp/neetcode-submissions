class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums) 
        if total % 2 != 0:
            return False 
        target = total // 2 

        cache = {} 

        def dfs(i, remaining):
            if remaining == 0:
                return True 
            if remaining < 0 or i >= len(nums):
                return False 
            if (i,remaining) in cache:
                return cache[(i,remaining)]

            cache[(i,remaining)] = (dfs(i+1 , remaining - nums[i]) or dfs(i + 1, remaining)) 
            return cache[i,remaining]

        return dfs(0,target) 

         
