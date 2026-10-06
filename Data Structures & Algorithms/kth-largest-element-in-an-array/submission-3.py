class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new = [-i for i in nums]
        heapq.heapify(new) 
        for _ in range(k-1):
            heapq.heappop(new) 
        return -heapq.heappop(new)