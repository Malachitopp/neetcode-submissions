class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l,r = 0,0 

        """go through and slide the window along. calculkate the max jump and move the window"""

        while r < len(nums) - 1:
            farthest = 0 
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i]) 
            #move your position, L is your current position. R is the end of the jump
            
            l = r + 1
            r = farthest 
            res += 1

            

        return res