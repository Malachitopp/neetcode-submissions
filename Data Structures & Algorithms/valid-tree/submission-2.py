
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        prereq = {c: [] for c in range(n)}
        for node, pre in edges:
            prereq[node].append(pre)
            prereq[pre].append(node) 

        visited = set() 
        cycle = set()
        def detect(node, prev): 
            if node in cycle:
                return False 
            if node in visited:
                return True 
            
            cycle.add(node) 
            for edge in prereq[node]:
                if edge != prev and not detect(edge,node) :
                    return False 
                
            visited.add(node)
            cycle.remove(node) 

            return True 
        
        detect(0,-1) 

        return len(visited) == n 

