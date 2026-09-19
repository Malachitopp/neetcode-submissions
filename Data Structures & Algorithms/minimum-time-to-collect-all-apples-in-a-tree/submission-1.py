class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {c:[] for c in range(n)}

        for crs, pre in edges:
            adj[crs].append(pre)
            adj[pre].append(crs) 
        
        def dfs(node, parent):
            time = 0 

            for nei in adj[node]:
                if nei == parent:
                    continue 
                timeTaken = dfs(nei, node) 
                if timeTaken > 0 or hasApple[nei]:
                    time += timeTaken + 2 
            return time 
        return dfs(0,-1) 

    
