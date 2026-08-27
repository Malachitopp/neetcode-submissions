class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l, r = 0,0

        while l < len(arr)-1:
            arr[l] = max(arr[l+1:])
                
            l += 1 
        arr[-1] = -1
        return arr 