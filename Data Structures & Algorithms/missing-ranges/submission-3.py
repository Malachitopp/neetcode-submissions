class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        output = [] 
        bounds = [lower - 1] + nums + [upper+1]

        for i in range(1, len(bounds)):
            if bounds[i] - bounds[i-1] > 1 :
                output.append([bounds[i-1]+1, bounds[i] - 1])
        
        return output