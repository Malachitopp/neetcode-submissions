class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = nums1, nums2

        total = len(a) + len(b) 
        half = total // 2

        if len(b) < len(a):
            a,b = b,a 

        l, r = 0, len(a) - 1
        while True: 
            i = (l + r) // 2
            j = half  -  i - 2

            Aleft = a[i] if i>= 0 else float("-inf")
            aright = a[i+1] if i + 1 < len(a) else float("infinity")
            
            bleft = b[j] if j >= 0 else float("-inf") 

            bright = b[j+1] if j+1 < len(b) else float("infinity")
            if Aleft <= bright and aright > bleft:
                if total % 2 != 0:
                    return min(aright, bright) 
                else:
                    return (max(Aleft, bleft) + min(aright, bright))/2
            elif Aleft > bright:
                r = i - 1
            else:
                l = i + 1