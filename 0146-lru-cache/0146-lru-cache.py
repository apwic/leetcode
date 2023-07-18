class LRUCache:

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.curr_capacity = 0
        self.LRU = None
        self.cache = {}
        self.queue = []

    def __updateLRU(self, key: int) -> None:
        self.queue.remove(key)
        self.queue.append(key)
        self.LRU = self.queue[0]
        
    def __addQueue(self, key: int) -> None:
        self.queue.append(key)
        self.LRU = self.queue[0]

    def get(self, key: int) -> int:
        if self.cache.get(key) == None:
            return -1
        
        self.__updateLRU(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if (self.get(key) != -1):
            self.__updateLRU(key)
        else:
            if (self.curr_capacity >= self.max_capacity):
                self.queue.remove(self.LRU)
                self.cache.pop(self.LRU)
            else:
                self.curr_capacity += 1
            
            self.__addQueue(key)

        self.cache[key] = value
