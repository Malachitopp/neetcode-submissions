class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        output = []

        def dfs(i, total):
            Sum = sum(total)  
            if Sum == target:
                output.append(total.copy()) 
                return
            if i >= len(candidates):
                return
            if Sum > target:
                return 
                
            total.append(candidates[i])
            dfs(i+1, total) 
            total.pop() 
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, total) 

        dfs(0,[]) 
        return output