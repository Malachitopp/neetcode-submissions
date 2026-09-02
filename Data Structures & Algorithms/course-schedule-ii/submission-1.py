class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre) 
        output = []
        completed = set() 
        cycle = set() 

        def dfs(course):
            if course in cycle:
                return False
            if course in completed:
                return True 
            
            cycle.add(course)
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
                
            cycle.remove(course)
            completed.add(course) 
            output.append(course) 
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output 