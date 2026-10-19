class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #store of the number and its index 
        store = {} 

        for i, num in enumerate(nums):
            remaining = target - num 
            if remaining in store:
                return [store[remaining], i] 
            store[num] = i 