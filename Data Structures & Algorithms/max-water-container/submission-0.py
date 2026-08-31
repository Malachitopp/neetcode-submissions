class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0  
        while l < r: 
            
            if heights[l] < heights[r]:
                height =  heights[l]
                area = height * (r-l) 
                l += 1
                
            else:
                height = heights[r]
                area = height * (r - l)
                
                r -= 1
            maxArea = max(maxArea, area)

        return maxArea

