class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre) 
            
        cycle = set() 
        visited =set() 
        output = [] 
        def dfs(course):
            if course in cycle:
                return False 
            if course in visited:
                return True 
            
            cycle.add(course)
            for i in prereq[course]:
                if not dfs(i):
                    return False 
            
            cycle.remove(course) 
            visited.add(course) 
            output.append(course)
            return True 
       
        for i in range(numCourses):
            if not dfs(i):
                return [] 

        return output 