class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        counter = {} 
        output = "" 

        for ch in s:
            counter[ch] = counter.get(ch,0) + 1 
        
        for key, value in counter.items():
            heapq.heappush(heap, (-value, key))
            if -value > math.ceil(len(s) /2):
                return "" 
        
        while heap:
            maximum, key = heapq.heappop(heap) 
            if not output or key != output[-1]:
                 
                output += key 
                maximum += 1
                if maximum < 0:
                    heapq.heappush(heap, (maximum, key)) 
            else: 
                if not heap:
                    return "" 
                max2, key2 = heapq.heappop(heap) 
                output += key2 
                max2 += 1 
                if max2 < 0:
                    heapq.heappush(heap, (max2, key2))
                
                heapq.heappush(heap, (maximum, key)) 
        
        return output


            
        
   
        