class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.counter = 0 
        self.height = height 
        self.width = width 
        self.food = food 
        self.snake = deque([(0,0)]) 
        self.occupied = set([(0,0)])
        self.directions = {"U":[-1,0], "D":[1,0],"R":[0,1], "L":[0,-1]}

        


    def move(self, direction: str) -> int:
        dr, dc = self.directions[direction]
        r, c = self.snake[-1]
        new_head = (r+dr, c+ dc)
        if not 0 <= new_head[0] < self.height:
            return -1 
        if not 0<= new_head[1] < self.width:
            return -1 
        
        if self.counter < len(self.food) and self.food[self.counter] == list(new_head):
            self.counter += 1 
        else:
            tail = self.snake.popleft() 
            self.occupied.remove(tail) 

        if new_head in self.occupied:
            return -1 
        self.snake.append(new_head)
        self.occupied.add(new_head) 

        return self.counter



        

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
