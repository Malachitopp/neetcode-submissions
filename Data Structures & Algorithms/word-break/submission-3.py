class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        adj = [False] * (len(s)+1 )
        adj[len(s)] = True 

        for i in reversed(range(len(s))):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i +len(w)] == w: 
                    adj[i] = adj[i + len(w)]
                if adj[i]:
                    break 
        return adj[0] 

