class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0 
        maxOnes = 0 
        zeros = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1 
            
            while zeros >  1:
                if nums[l] == 0:
                    zeros -= 1 
                l += 1
            maxOnes = max(maxOnes, i - l + 1)
        
        return maxOnes 

        
