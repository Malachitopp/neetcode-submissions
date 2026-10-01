class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        output = []
        if len(s) > 12:
            return output 

        def dfs(i, dots, curIP):
            if dots == 4 and i ==len(s):
                output.append(curIP[:-1])
                return 
            if dots>4:
                return 

            for j in range(i, min(i+3, len(s))):
                if i != j and s[i] == '0':
                    continue 
                if int(s[i:j+1]) < 256:
                    dfs(j+1, dots + 1, curIP + s[i:j+1] + '.')

        dfs(0,0,"")
        return output 

            