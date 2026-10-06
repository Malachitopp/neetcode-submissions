class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = [] 

        def dfs(curr,i):
            Sum = sum(curr)
             
            if Sum == target:
                output.append(curr.copy())
                return 
            if i >= len(candidates):
                return
            if Sum > target:
                return 

            curr.append(candidates[i])
            dfs(curr, i + 1) 
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(curr, i+1)

        dfs([],0)
        return output