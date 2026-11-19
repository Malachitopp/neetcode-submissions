class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        goodPairs = {} 

        for i, num in enumerate(nums):
            key = num - i
            goodPairs[key] = goodPairs.get(key,0) + 1 
        good = 0 
        for values in goodPairs.values():
            good += self.choose(values)

        totalPairs = self.choose(len(nums))
        return totalPairs - good 

        
    def choose(self, k):
        return (k * (k-1))//2 