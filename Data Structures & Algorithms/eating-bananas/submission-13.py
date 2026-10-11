class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        slowest, fastest = 1, max(piles) 

        while slowest < fastest:
            mid = (slowest + fastest) // 2 
            total = 0 
            for banana in piles:
                tk = math.ceil(banana/ mid) 
                total += tk 

            if total > h:
                slowest = mid + 1
            else:
                fastest = mid 
            
        return slowest 