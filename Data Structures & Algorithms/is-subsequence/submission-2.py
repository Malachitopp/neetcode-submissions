class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # index into s
        j = 0  # index into t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)