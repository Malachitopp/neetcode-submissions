class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        prefix = {0: -1 } 
        res = 0 
        curr = 0 

        for i, num in enumerate(nums):
            curr += num
            remainder = curr % k 
            if remainder not in prefix:
                prefix[remainder] = i
            elif i - prefix[remainder] > 1:
                return True

        


        return False