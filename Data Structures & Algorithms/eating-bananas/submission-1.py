class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k):
            return sum((p+k-1)//k for p in piles)
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right)//2
            if hours_needed(mid) <= h :
                right = mid
            else:                        # too slow → need faster
                left = mid + 1
        return left


        