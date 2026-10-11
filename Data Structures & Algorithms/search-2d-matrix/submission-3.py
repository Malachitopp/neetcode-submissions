class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        colStart, colEnd = 0,len(matrix)-1
         
        while colStart < colEnd:
            mid = (colEnd + colStart) // 2 
            if matrix[mid][-1] >= target:
                colEnd = mid
            else: 
                colStart=mid+1

        targetRow = colStart
        rowStart, rowEnd = 0, len(matrix[0]) - 1
        answer = None 
        while rowStart <= rowEnd:
            mid = (rowStart + rowEnd) // 2 
            if matrix[targetRow][mid] > target:
                rowEnd = mid - 1
            elif matrix[targetRow][mid] < target:
                rowStart = mid + 1
            else:
                answer = matrix[targetRow][mid] 
                break 

        return answer == target
