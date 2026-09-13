class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        appeared = set(nums) 
        output = [] 

        for num in range(1,len(nums)+1):
            if num not in appeared:
                output.append(num) 
            
        return output 