class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i : i[0])
        output = [intervals[0]]

        for i in range(1, len(intervals)):
            if output[-1][1] <intervals[i][0]:
                output.append(intervals[i])
            if output[-1][1] < intervals[i][1]:
                output[-1][1] = intervals[i][1]
            
            
        return output 
        