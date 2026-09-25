class MovingAverage:

    def __init__(self, size: int):
        self.window = deque() 
        self.size = size 
    def next(self, val: int) -> float:
         
        while self.window and len(self.window) >= self.size:
            self.window.popleft() 
        self.window.append(val) 
        denominator = len(self.window)
        
        total = sum(self.window) 
        return total/denominator 



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
