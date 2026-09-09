class StockSpanner:

    def __init__(self):
        self.counter =  1
        self.store = [] 

    def next(self, price: int) -> int:
        count = 0
        self.store.append(price) 
        i = self.counter 
        while i > 0 and self.store[i-1] <= self.store[self.counter -1  ]:
            count += 1 
            i -= 1 
        self.counter += 1 
        return count 
        




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)