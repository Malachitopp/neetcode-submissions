class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            leftHalf = arr[:mid]
            rightHalf = arr[mid:]

            sortedLeft = mergeSort(leftHalf)
            sortedRight = mergeSort(rightHalf)

            return merge(sortedLeft, sortedRight)

        def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])

            return result

        
        merged = merge(nums1, nums2) 
        merged = mergeSort(merged)
        mid=len(merged) //2 
        print(merged)
        if len(merged) % 2 != 0 :
            return merged[mid]
        else:
            return (merged[mid ] + merged[mid-1]) /2 

