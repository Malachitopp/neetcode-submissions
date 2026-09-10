class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        l = 0 
        r = 1
        while r < len(nums):
           
            if nums[r] % 2 != 0 and nums[l]%2 != 0 or nums[r] % 2 == 0 and nums[l] % 2 == 0:
                return False 
            
       

                
            l += 1 
            r += 1 
        return True

