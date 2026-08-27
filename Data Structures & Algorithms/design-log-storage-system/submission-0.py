class LogSystem:

    def __init__(self):
        self.logsystem = {} 
        self.granularity = {"Year":4, "Month":6, "Day":8, "Hour":10, "Minute":12, "Second":14}
        

    def put(self, id: int, timestamp: str) -> None:
        self.logsystem[id] = timestamp 

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        self.output = []
        def replacement(string):
            return string.replace(":", "")
        start = replacement(start)
        end = replacement(end) 
        n = self.granularity[granularity]

        for key, value in self.logsystem.items():
            if start[:n] <= replacement(value)[:n] <= end[:n]:
                    self.output.append(key) 
        
        return self.output




        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
