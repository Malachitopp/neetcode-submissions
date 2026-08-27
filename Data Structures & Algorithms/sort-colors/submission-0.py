class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0 
        white = 0 
        blue = 0 
        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            else:
                blue += 1

        bucket = [red,white,blue]
        organised = []
        for colour in range(len(bucket)):
            count = bucket[colour]
            for _ in range(count):
                organised.append(colour)
        nums[:] = organised
        return nums
