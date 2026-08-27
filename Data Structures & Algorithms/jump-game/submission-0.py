class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """ pos that can reach the end? 
        move backwards 
        if at position i, you can reach the goal, index i becomes the new goal. THen you as you move backwards, you have a target to hit, otherwise Return False 
        if index 0 is goal return true"""
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1 ):
            if i + nums[i] >= goal: #dont have to jump the max amount. So if goal is within that jump range then you can set it equal to i 
                goal = i 
        return goal == 0 