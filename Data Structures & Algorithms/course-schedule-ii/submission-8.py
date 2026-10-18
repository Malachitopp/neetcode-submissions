class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c:[] for c in range(numCourses)}

        for pre, nei in prerequisites:
            adj[pre].append(nei)
        cycle = set() 
        completed = set() 
        output = [] 
        def dfs(course):
            if course in cycle:
                return False 
            if course in completed:
                return True 
            
            cycle.add(course)
            for nei in adj[course]:
                if not dfs(nei):
                    return False 
            cycle.remove(course) 
            completed.add(course) 
            output.append(course) 
            return True 
        
        for i in range(numCourses):
            if not dfs(i):
                return [] 
        
        return output
