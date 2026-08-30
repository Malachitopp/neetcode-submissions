class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated_digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}

        l = 0
        r = len(num)- 1

        while l <= r:
            if num[l] not in rotated_digits or rotated_digits[num[l]] != num[r] :
                return False
            l += 1
            r-= 1
        
        return True
            




