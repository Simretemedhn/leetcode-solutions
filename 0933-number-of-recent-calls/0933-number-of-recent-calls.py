from collections import deque
class RecentCounter:

    def __init__(self):
        self.queue = deque()
        self.start = 0 

    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.start = t - 3000 
        while self.queue and self.queue[0] < self.start:
            self.queue.popleft()
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t) 