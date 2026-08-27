class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        c = 0

        ans = []
        while c < 2:
            for num in nums:
                ans.append(num) 
            c += 1
        return ans 