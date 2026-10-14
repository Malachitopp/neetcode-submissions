class Solution:
    def numDecodings(self, s: str) -> int:
        
        cache = {} 

        def dfs(i):
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0 
            if i in cache:
                return cache[i]

            total = dfs(i+1) 

            if s[i] == '1' and i+1 < len(s) :
                if s[i+1] in set('0123456789'):
                    total += dfs(i+2)

            if s[i] == '2' and i + 1 < len(s) :
                if s[i+1] in set('0123456'):
                    total += dfs(i+2)


            cache[i] = total 
            return total 
        
        return dfs(0) 

                