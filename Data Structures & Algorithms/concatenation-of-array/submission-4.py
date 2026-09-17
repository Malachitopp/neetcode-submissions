class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        copy = nums.copy() 

        for num in nums:
            copy.append(num)
        return copy