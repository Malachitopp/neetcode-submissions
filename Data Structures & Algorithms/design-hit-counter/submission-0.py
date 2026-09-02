class HitCounter:

    def __init__(self):
        self.counter = {} #timestamp, number of hits 



    def hit(self, timestamp: int) -> None:
        self.counter[timestamp] = self.counter.get(timestamp,0) + 1

    def getHits(self, timestamp: int) -> int:
        total = 0
        for time, hits in self.counter.items():
            if timestamp - 300 < time <= timestamp:
                total += hits
        return total
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
