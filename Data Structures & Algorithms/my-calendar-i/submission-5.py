class MyCalendar:
    
    def __init__(self):
        self.store=[] 

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.store:
            self.store.append([startTime, endTime])
            return True
        for start, end in self.store:
            if startTime < end and endTime > start:
                return False
           
        self.store.append([startTime,endTime])
        return True 


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)