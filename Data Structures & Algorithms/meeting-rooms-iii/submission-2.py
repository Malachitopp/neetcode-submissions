class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = [i for i in range(n)]
        count = [0] * n 

        heap = []   

        for start, end in meetings: 
            while heap and start > heap[0][0]:
                _, room = heapq.heappop(heap) 
                heapq.heappush(available, room)

            if not available:
                smallestend, room = heapq.heappop(heap) 
                end = smallestend + (end - start) 
                heapq.heappush(available, room) 
            room = heapq.heappop(available) 
            heapq.heappush(heap, (end, room))
            count[room] += 1 
        
        return count.index(max(count)) 
            