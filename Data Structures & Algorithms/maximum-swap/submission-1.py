class Solution:
    def maximumSwap(self, num: int) -> int:
        

        i = 0 
        nums = list(str(num)) 
        while i+1   < len(nums) and int(nums[i] ) >= int(nums[i+1]):
            i+=1 
        if i == len(nums) - 1:
            return num 
        toSwap = i+1
        store = {} 
        for j in range(i+1, len(nums)):
            if nums[j] >= nums[toSwap]:
                toSwap = j
            
        
        for k in range(i+1):
            if nums[k] < nums[toSwap]:
                nums[k], nums[toSwap] = nums[toSwap], nums[k]
                break 
        
        return int("".join(nums)) 
        

        
