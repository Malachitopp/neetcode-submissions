class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i) 
        tasks.sort(key = lambda item: item[0])
        heap = [] 
        output = [] 
        time = tasks[0][0] 
        i = 0 
        while heap or i < len(tasks):
            while i < len(tasks ) and time >= tasks[i][0]:
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]]) 
                i += 1 
            if not heap:
                time = tasks[i][0]
            else:
                timeTaken, index = heapq.heappop(heap) 
                output.append(index) 
                time += timeTaken 
            
        return output 