class RecentCounter:

    def __init__(self):
        from collections import deque
        self.queue = deque([])

    def ping(self, t: int) -> int:
        self.queue.append(t)
        val = self.queue[0]
        mn = t-3000
        while val < mn:
            self.queue.popleft()
            val = self.queue[0]

        return len(self.queue)
    
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)