class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0] * (len(self.nums))
        count = 0 
        for i in range(len(self.nums)):
            count += self.nums[i]
            self.prefix[i] += count 
        self.prefix = [0] + self.prefix 
    def sumRange(self, left: int, right: int) -> int:
        print(self.prefix)
        return self.prefix[right+1] - self.prefix[left]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)