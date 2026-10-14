class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {} 
        for task in tasks:
            counter[task]= counter.get(task, 0 ) + 1 
        occ = [-i for i in counter.values() ]
        heapq.heapify(occ)

        time = 0 
        q = deque() 
        # holds the [occurances, time remaining]
        while q or occ: 
            time +=1 
            if occ:
                occLeft= heapq.heappop(occ) + 1 
                if occLeft != 0 :
                    q.append([occLeft, time + n])
            if q and q[0][1] == time:
                occLeft, _ = q.popleft() 
                heapq.heappush(occ, occLeft)

        return time 
