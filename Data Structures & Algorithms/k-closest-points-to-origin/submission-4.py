class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance =[]
        for point in points:
            diagonal = point[0]**2 + point[1]**2 
            heapq.heappush(distance,[diagonal, point]) 
        
        res = []
        for _ in range(k):
            _, point = heapq.heappop(distance)
            res.append(point)

        return res