class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        start = n - k

        groupB = nums[start:]

        for letter in nums[:start]:
            groupB.append(letter)

        nums[:] = groupB