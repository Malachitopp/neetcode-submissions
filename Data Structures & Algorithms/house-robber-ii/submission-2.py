class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = {} 

        def dfs(i: int,flag: bool) -> int:
            if i >= len(nums):
                return 0 
            if i == len(nums) - 1 and flag:
                return 0
            if (i,flag) in cache:
                return cache[(i,flag)]
            
            cache[(i,flag)] = max(dfs(i+1, flag), nums[i] + dfs(i+2, flag or i == 0)) 
        
            return cache[(i,flag)] 
        
        return max(dfs(0, False), dfs(0, True)) 
