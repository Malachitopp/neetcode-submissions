class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        prereq = {c: [] for c in range(n)}

        for node, pre in edges:
            prereq[node].append(pre) 
            prereq[pre].append(node)
        
        visited = set() 
       
        output = 0 
        def dfs(node):
            nonlocal output 
            visited.add(node) 
            for nei in prereq[node]:
                if nei not in visited:
                        dfs(nei) 
            
           

          
        
        for i in range(n):
            if i not in visited:
                output += 1
                dfs(i) 
            
        return output 

