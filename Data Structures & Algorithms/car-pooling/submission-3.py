class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda i: i[1])
        heap = [] #passengers, end  
        cur = 0 

        for num, start, end in trips:
            while heap and heap[0][0] <= start:
                cur -= heapq.heappop(heap)[1]
            cur += num 
            if cur > capacity:
                return False 
            heapq.heappush(heap, [end, cur])
        
        return True 