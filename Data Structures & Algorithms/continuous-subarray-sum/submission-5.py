class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = {0:-1} 
        count = 0 


        for i, num in enumerate(nums):
            count += num 
            remainder = count % k 

            if remainder not in prefix:
                prefix[remainder] = i 
            elif i - prefix[remainder] >1 :
                return True 
            

        return False 
            
            
            