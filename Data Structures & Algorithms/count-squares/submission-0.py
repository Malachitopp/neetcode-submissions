class CountSquares:

    def __init__(self):
        self.square = {} 

    def add(self, point: List[int]) -> None:
        self.square[(point[0],point[1])] = self.square.get((point[0],point[1]), 0) + 1 

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point 

        for (x, y ), count in self.square.items() :
            if (abs(py - y) != abs(px- x)) or x==px or y ==py:
                continue
            res += count * self.square.get((x, py), 0) * self.square.get((px, y), 0) 
        return res 
