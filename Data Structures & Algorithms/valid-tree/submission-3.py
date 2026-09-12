class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        prereq = {c:[] for c in range(n)}

        for node, pre in edges:
            prereq[node].append(pre) 
            prereq[pre].append(node)

        visited = set() 
        cycle = set() 

        def dfs(node, prev):
            if node in visited:
                return True 
            if node in cycle:
                return False

            cycle.add(node) 
            for pre in prereq[node]:
                if not dfs(pre, node ) and prev!=  pre :
                    return False 
                
            
            visited.add(node) 
            cycle.remove(node) 
            return True 
        
        dfs(0,-1) 
    
        return len(visited) == n 