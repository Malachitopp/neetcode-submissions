class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {c:[] for c in range(n)}
        for pre, nei in edges:
            adj[pre].append(nei)
            adj[nei].append(pre) 

        visited = set() 

        def dfs(node):
            visited.add(node) 
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei) 
        output = 0 
        for i in range(n):
            if i not in visited:
                output += 1 
                dfs(i) 

        return output 