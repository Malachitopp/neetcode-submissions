class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {} 

        def dfs(i,j,k):
            if k == len(s3):
                return True if (i == len(s1) and j == len(s2)) else False

            if (i,j,k) in cache:
                return cache[(i,j,k)]
            ans = False
            if i < len(s1) and s1[i] == s3[k]:
                ans = dfs(i+1, j, k+1)
            if not ans and j < len(s2) and s2[j] == s3[k]:
                ans = dfs(i, j +1, k+1)
            cache[(i,j,k)] = ans
            return cache[(i,j,k)] 
            
        return dfs(0,0,0)