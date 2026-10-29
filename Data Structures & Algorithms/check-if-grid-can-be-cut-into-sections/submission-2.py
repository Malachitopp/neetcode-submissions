class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x, y = [], [] 
        for interval in rectangles:
            x.append([interval[0],interval[2]])
            y.append([interval[1],interval[3]])

        x.sort() 
        y.sort() 

        def searchInterval(intervals):
   
            stack = [intervals[0]] 
            for i in range(1,len(intervals)):
                if intervals[i][0] >= stack[-1][1]:
                    stack.append(intervals[i])
                    continue 
                if intervals[i][1] > stack[-1][1]:
                    stack[-1][1] = intervals[i][1]
                    continue 

            
            return len(stack)

        return max(searchInterval(x), searchInterval(y)) >= 3
