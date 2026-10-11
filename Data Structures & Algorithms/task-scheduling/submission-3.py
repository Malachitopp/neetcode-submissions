class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count  = {} 
        for task in tasks:
            count[task] = count.get(task, 0) + 1 
        occ = [-i for i in count.values()]
        heapq.heapify(occ) 


        q = deque() 
        time = 0 
        while occ or q :
            time += 1 
            if occ:
                most = heapq.heappop(occ) +1
                if most != 0:
                    q.append([most, time + n ])

            
             
            if q and q[0][1] == time:
                a,b = q.popleft() 
                heapq.heappush(occ, a)

        return time 
            
                