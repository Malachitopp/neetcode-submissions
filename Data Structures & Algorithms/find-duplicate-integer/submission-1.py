class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        store = {} 
        for i, num in enumerate(nums):
            store[num] = store.get(num, 0) + 1 
        
        for num, value in store.items():
            if value > 1:
                return num