class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {c: [] for c in range(numCourses)}
    
        for crs, pre in prerequisites:
            prereq[crs].append(pre) 
        visited = set() 
        cycle = set() 
        def dfs(course):
            if course in cycle:
                return False 
            if course in visited:
                return True 
            
            cycle.add(course) 
            for pre in prereq[course]:
                if not dfs(pre):
                    return False 
            
            cycle.remove(course) 
            visited.add(course) 
            return True 
        
        for c in range(numCourses):
            if not dfs(c):
                return False 
            
        return True 

            