class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {c:[] for c in range(1,len(edges)+1)}

  

   
        completed = set() 

      
        def dfs(node, target):
            if node ==target:
                return True 

            completed.add(node) 
            for nei in adj[node]:
                if nei not in completed and dfs(nei, target):
                    return True 
            completed.remove(node)
            return False 
        
        for a, b in edges:
            if dfs(a,b):
                return [a,b] 
            adj[a].append(b)
            adj[b].append(a) 
                