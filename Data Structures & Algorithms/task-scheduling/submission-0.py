class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = {}
        for t in tasks:
            counts[t] = counts.get(t, 0) + 1
        occurences = [-i for i in counts.values()]
        heapq.heapify(occurences)

        q=deque() 
        time = 0 
        while occurences or q:
            time += 1
            if occurences:
                count = heapq.heappop(occurences) + 1 
                if count != 0:
                    q.append([count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(occurences, q.popleft()[0])
        return time