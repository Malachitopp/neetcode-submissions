class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val 
        self.counter = 1 
        self.prev = self.next = None 

class DlinkedList:
    def __init__(self):
        self.left, self.right = Node(0,0), Node(0,0) 
        self.left.next, self.right.prev = self.right, self.left 
        self.size = 0 
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right 
        prev.next = nxt.prev = node 
        node.next, node.prev = nxt, prev 
        self.size += 1
    
    def remove(self,node):
        prev, nxt = node.prev, node.next 
        prev.next, nxt.prev = nxt, prev 
        self.size -= 1 

    def pop_lru(self):
        node = self.left.next 
        self.remove(node)
        return node 


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.store = {}
        self.buckets = defaultdict(DlinkedList) 
        self.minFreq = 0 


    def touch(self, node):
        f = node.counter 
        self.buckets[f].remove(node) 
        if self.buckets[f].size == 0 and self.minFreq == f:
            self.minFreq = f + 1
        node.counter += 1
        self.buckets[node.counter].insert(node) 

    def get(self, key: int) -> int:
        if key not in self.store:
            return - 1
        node = self.store[key] 
        self.touch(node) 

        return node.val 
    

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return 
        
        if key in self.store:
            node = self.store[key]
            node.val = value 
            self.touch(node) 
            return 
        
        if len(self.store) >= self.capacity:
            victim = self.buckets[self.minFreq].pop_lru() 
            del self.store[victim.key] 

        node = Node(key,value) 
        self.store[key] = node
        self.buckets[1].insert(node) 
        self.minFreq = 1 

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)