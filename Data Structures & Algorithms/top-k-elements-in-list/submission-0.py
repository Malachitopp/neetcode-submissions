class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {} 
        for num in nums:
            store[num] = store.get(num,0) + 1 
        
        sorted_items = sorted(store.items() , key = lambda item: item[1], reverse = True)

        return [num for num, count in sorted_items[:k]]



        
