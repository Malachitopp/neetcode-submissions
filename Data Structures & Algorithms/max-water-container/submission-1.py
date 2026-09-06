class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r= 0, len(heights) - 1
        maxArea = 0 
        while l< r:
            if heights[l] <= heights[r]:
                area = heights[l] * (r-l)
                maxArea = max(maxArea, area) 
                l +=1  
            else:
                area = heights[r] * (r-l)
                maxArea = max(maxArea, area)
                r -= 1 
            
        return maxArea 