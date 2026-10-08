class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {} 

        def dfs(l,r):
            if l == r:
                return 1
            if l > r:
                return 0
            if (l,r) in cache:
                return cache[(l,r)]
            
            if s[l] == s[r]:
                cache[(l,r)] = 2 + dfs(l+1, r-1)
            else:
                cache[(l,r)] = max(dfs(l, r-1),  dfs(l+1, r))
            return cache[(l,r)]

        return dfs(0, len(s) -1)