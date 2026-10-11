class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones) 
        if not stones:
            return 0 

        while len(stones) >1:
            x = heapq.heappop(stones) 
            y = heapq.heappop(stones) 
            if x == y:
                continue 
            if x < y:
                new = x-y
                heapq.heappush(stones, new) 
        
        return -1 * stones[0] if stones else 0 