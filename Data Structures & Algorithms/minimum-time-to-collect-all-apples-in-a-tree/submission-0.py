class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {c:[] for c in range(n)}

        for node, nei in edges:
            adj[node].append(nei) 
            adj[nei].append(node)
        

        def dfs(node, nei):
            time = 0 

            for neighbour in adj[node]:
                if neighbour == nei:
                    continue
                childtime = dfs(neighbour, node)
                if childtime > 0 or hasApple[neighbour]:
                    time += 2 + childtime
            
            return time 
        
        return dfs(0,-1) 
