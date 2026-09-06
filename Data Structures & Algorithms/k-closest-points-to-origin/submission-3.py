class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minDistance = 2**31
        output = []
        store = {} 
        for point in points:
            distance2 = point[0]**2 + point[1]**2
            store[(point[0],point[1])] = distance2 

        distances = sorted(store.items() , key = lambda item: item[1])
        for key, val in distances:
            if len(output) < k:
                output.append(key) 
            
        return output 
            




