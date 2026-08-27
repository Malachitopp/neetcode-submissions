class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0 
        current = 0
        for i in nums:
            if i == 1:
                current += 1
                best = max(best,current)
            else:
                current = 0
        return best