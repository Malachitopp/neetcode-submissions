class CountSquares:

    def __init__(self):
        self.store = {} 

    def add(self, point: List[int]) -> None:
        self.store[(point[0],point[1])] = self.store.get((point[0],point[1]), 0) + 1 

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point 

        
        for (x,y), count in self.store.items():
            if abs(px - x) == abs(py - y) and x != px and y != py:
                res += count * self.store.get((px,y),0) * self.store.get((x,py),0)
        return res 