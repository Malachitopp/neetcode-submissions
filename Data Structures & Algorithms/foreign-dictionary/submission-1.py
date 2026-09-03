class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        prereq = {c: set() for w in words for c in w  }
    
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2)) 
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return "" 
            for j in range(minLen):
                if w1[j] != w2[j]:
                    prereq[w1[j]].add(w2[j]) 
                    break 
                
        visited = set() 
        cycle = set() 
        res = [] 

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)

            for nei in prereq[course]:
                if not dfs(nei):
                    return False 
            

            cycle.remove(course)
            visited.add(course) 

            res.append(course) 
            return True 
        
        for course in prereq:
            if not dfs(course):
                return "" 
        
        res.reverse() 
        return "".join(res) 
