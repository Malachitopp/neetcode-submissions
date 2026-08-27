class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)

        top = 0
        bottom = m- 1

        while top <= bottom:
            mid = (top + bottom) // 2 
            if target > matrix[mid][-1]:
                top = mid + 1 
            elif target  < matrix[mid][0]:
                bottom = mid - 1
            else:
                break 
        else:
            return False

        left = 0
        right = len(matrix[mid]) - 1

        while left <= right:
            middle = (left+right)//2
            if target > matrix[mid][middle]:
                left = middle + 1
            elif target< matrix[mid][middle]:
                right = middle - 1
            else: 
                return True
        return False
