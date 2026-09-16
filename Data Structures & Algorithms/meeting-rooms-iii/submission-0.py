class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda i: i[0])
        available = [i for i in range(n)] 
        used = []
        count = [0] * n 


        for start, end in meetings:
            while used and start >= used[0][0]:
                _, room = heapq.heappop(used)
                heapq.heappush(available,room)
            if not available:
                end_time, room = heapq.heappop(used)
                end = end_time + (end - start) 
                heapq.heappush(available, room) 
            
            room = heapq.heappop(available) 
            heapq.heappush(used, (end, room)) 
            count[room] += 1 

        return count.index(max(count)) 

"""The flow is, to go through the rooms, starting with every room available, you check, is there a room with a start that is greater than a rooms end? if there is then you need to push that room into occupied, and free the room whos ending was smaller than the current start. Otherwise, if there are no rooms available, then you need to pop the room ending soonest from the occupied rooms, and you need to delay the occupied room by the interval of the current room. Then you can treat that room as being freed up and available. If there is a room available, then you want to take it, and you want to push that room into the used heap, with either the ending of the current room, or the delayed ending of the previously occupied room. Incremnent the count of the room, and return the room with the most appearences"""


                
            
