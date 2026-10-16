class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {c:[] for c in range(n)}
        for pre, nei in edges:
            adj[pre].append(nei)  
            adj[nei].append(pre)
        completed = set() 
        cycle = set() 

        def dfs(node,prev):
            if node in cycle:
                return False 
            if node in completed:
                return True 
            
            cycle.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue 
                if not dfs(nei,node):
                    return False 
                
            cycle.remove(node) 
            completed.add(node) 
            return True 
        dfs(0,-1) 

         
        return len(completed) == n 