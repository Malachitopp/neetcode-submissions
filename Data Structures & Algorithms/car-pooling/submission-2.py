class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort( key= lambda i: i[1])
        heap = [] 
        cur = 0 
        for trip in trips:
            while heap and heap[0][0] <= trip[1]:
                cur -= heapq.heappop(heap)[1] 
            cur += trip[0] 
            if cur > capacity:
                return False 
            heapq.heappush(heap, [trip[2], trip[0]])

        return True 