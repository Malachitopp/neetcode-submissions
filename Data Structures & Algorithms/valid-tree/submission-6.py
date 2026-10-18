class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {c:[] for c in range(n)}

        for node, nei in edges:
            adj[nei].append(node) 
            adj[node].append(nei) 

        visited = set()
        cycle = set()  
        def dfs(node, parent):
            if node in cycle:
                return False 
            if node in visited:
                return True 
            cycle.add(node) 
            for nei in adj[node]:
                if nei == parent:
                    continue 
                if not dfs(nei, node):
                    return False 
            visited.add(node) 
            cycle.remove(node) 
            return True 
        
        dfs(0, -1)
        return len(visited) == n 