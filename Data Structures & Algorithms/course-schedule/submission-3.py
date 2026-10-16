class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {c:[] for c in range(numCourses)}
        for pre, nei in prerequisites:
            adj[pre].append(nei)

        cycle = set() 
        visited = set( )
        def dfs(node):
            if node in visited:
                return True 
            if node in cycle:
                return False 
            
            cycle.add(node)
            for neighbour in adj[node]:
            
                if not dfs(neighbour):
                    return False 
            cycle.remove(node)
            visited.add(node)
            return True 
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True 