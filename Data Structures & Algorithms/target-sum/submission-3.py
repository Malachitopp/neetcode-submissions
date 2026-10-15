class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {} 

        def dfs(i, remaining):
            # we only have the base case after i is the length of the list 
            if i == len(nums):
                return 1 if remaining == 0 else 0
            
            if (i, remaining) in cache:
                return cache[(i,remaining)]
            #either add or subtract nums[i] and dfs returns the number of ways at i  
            cache[(i,remaining)] = dfs(i+1, remaining + nums[i]) + dfs(i +1, remaining - nums[i] )
            return cache[(i,remaining)]

        return dfs(0, target)