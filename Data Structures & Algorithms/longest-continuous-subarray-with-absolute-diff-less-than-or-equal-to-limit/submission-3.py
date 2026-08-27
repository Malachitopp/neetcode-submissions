class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q = deque() 
        min_q = deque() 

        l = 0 
        res = 0
        for i in range(len(nums)):
            while max_q and nums[i] > max_q[-1]:
                max_q.pop()
            while min_q and nums[i] < min_q[-1]:
                min_q.pop() 
            
            max_q.append(nums[i])
            min_q.append(nums[i]) 

          
            while max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[l]:
                    max_q.popleft()
                if min_q[0] == nums[l]:
                    min_q.popleft() 
                l += 1
            res = max(res, i - l + 1 )
        return res 

        