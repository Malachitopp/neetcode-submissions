class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        #Create max heap of the amount of times a letter appears 
        for t in tasks:
            counter[t]=counter.get(t,0) + 1 
        occurances = [-i for i in counter.values() ]
        heapq.heapify(occurances) 

        #create a queue that will store [occurances, expirary time]
        q = deque() 
        time = 0 
        while occurances or q:
            time += 1 #increment time every loop 
            if occurances:
                #if there are occurances then you need to add to queue 
                count = heapq.heappop(occurances) + 1 
                if count != 0:
                    q.append([count, time + n]) # time + n is when it expires 
            if q and q[0][1] == time:
                #if the letter has expired then you can add it back the heap 
                heapq.heappush(occurances, q.popleft()[0]) 
            
        return time 