from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.value = value
        self.k = k
        self.count = 0

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.value:
            self.count += 1
        if len(self.queue)<self.k:
            return False 
        elif len(self.queue) == self.k:
            return self.count == self.k
        else:
            val = self.queue.popleft()
            if val == self.value:
                self.count -= 1
        return self.count == self.k

""" or shortly using counter without the concept of queue 
def consec(self, num: int) -> bool:
    if num == self.value:
        self.count += 1
    else:
        self.count = 0
    return self.count >= self.k """


        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)