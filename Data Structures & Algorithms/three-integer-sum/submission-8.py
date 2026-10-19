class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = [] 

        nums.sort() 

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            l = i + 1 
            r = len(nums) - 1 
            while l < r: 
                summation = num + nums[l] + nums[r] 
                
                if summation > 0:
                    r -= 1 
                elif summation < 0:
                    l += 1 
                else:
                    output.append([num, nums[l], nums[r]])
                    l += 1 
                    r -= 1 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1 
            
        return output 