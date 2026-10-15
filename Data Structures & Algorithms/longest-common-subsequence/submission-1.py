class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {} 

        def dfs(l1, l2):
            if l1 >= len(text1) or l2 >= len(text2):
                return 0
            if (l1, l2) in cache:
                return cache[(l1,l2)]
            if text1[l1] == text2[l2]:
                cache[(l1,l2)] = 1 + dfs(l1+1, l2+1)
            else:
                cache[(l1,l2)] = max(dfs(l1+1, l2), dfs(l1, l2 + 1))
            
            return cache[(l1,l2)]
        return dfs(0,0) 