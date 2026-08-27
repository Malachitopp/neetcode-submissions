class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        for scan in range(len(nums)):
            if nums[scan] != 0:
                nums[write], nums[scan] = nums[scan], nums[write]
                write += 1 