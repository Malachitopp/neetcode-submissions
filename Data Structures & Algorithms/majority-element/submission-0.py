class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2 

        store = {} 

        for num in nums:
            store[num] = store.get(num, 0) + 1 
        
        for item, value in store.items():
            if value > majority:
                return item 