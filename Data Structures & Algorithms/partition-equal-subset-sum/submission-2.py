class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total % 2 != 0:
            return False 
        target = total//2
        cur = []
     

        def dfs(i):
            if sum(cur) == target :
                return True 
            if i >= len(nums) or sum(cur) > target:
                return False
            
            cur.append(nums[i]) # check array with current posiution added  
            if dfs(i+1):
                return True  
            cur.pop() 
            # check array by skipping 
            return dfs(i +1)
        
        return dfs(0 ) 
            