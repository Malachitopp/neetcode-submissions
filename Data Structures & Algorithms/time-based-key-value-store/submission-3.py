class TimeMap:

    def __init__(self):
        self.store = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key,0)
        if not values:
            return "" 
        
        l,r = 0, len(values) 
        while l<r:
            mid = (l+r)//2
            if values[mid][0] <= timestamp:
                l = mid +1
            else:
                r = mid 

        return values[l-1][1] if l != 0 else "" 