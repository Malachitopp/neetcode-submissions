class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        subject = []




        def dfs(i, total):
            if total == target:
                answer.append(subject.copy())
                return
            if i >= len(nums) or total > target:
                return

            subject.append(nums[i])
            dfs(i, total + nums[i])      # i, not i+1 — reuse allowed
            subject.pop()
            dfs(i + 1, total)  
        dfs(0,0)
        return answer           # move on, never use nums[i] again