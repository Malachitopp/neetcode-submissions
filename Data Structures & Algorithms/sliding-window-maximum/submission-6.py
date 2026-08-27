class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q =deque() 
        l = r = 0 

        while r < len(nums) :
            #while smaller values exist in the queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r) 
            #if number is outside of the window pop it
            if l > q[0]:
                q.popleft() 
            # if the edge of window is greater than or equal to its size, pick out the largest number and shift the left side forward
            if (r+1) >= k:
                res.append(nums[q[0]])
                l +=1 
                #shift window right
                
            r += 1 
        return res


            


        
        