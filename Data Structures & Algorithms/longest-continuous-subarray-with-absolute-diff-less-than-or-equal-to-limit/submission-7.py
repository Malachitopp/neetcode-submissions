class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq = deque() 
        minq = deque() 

        res = 0 
        l = 0 

        for i in range(len(nums)):
            while maxq and nums[i] > maxq[-1]:
                maxq.pop() 
            while minq and nums[i] < minq[-1]:
                minq.pop() 
            
            maxq.append(nums[i]) 
            minq.append(nums[i]) 

            while maxq[0] - minq[0] > limit:
                if maxq[0] == nums[l]:
                    maxq.popleft() 
                if minq[0] == nums[l]:
                    minq.popleft() 
                l += 1 
            res = max(res, i - l + 1) 
        
        return res