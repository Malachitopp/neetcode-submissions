class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0] )
        output = [intervals[0]] 

        for i in range(1,len(intervals)):
            end = output[-1][1] 
            if intervals[i][0] > end:
                output.append(intervals[i])
                continue
            if intervals[i][1] > end:
                output[-1][1] = intervals[i][1]
                continue 
             
        
        return output 