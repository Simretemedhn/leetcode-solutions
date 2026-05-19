from heapq import heappush, heappop, heapify 

class MedianFinder:

    def __init__(self):
        self.max_heap_left = [] 
        self.min_heap_right = []

    def addNum(self, num: int) -> None:
        if not self.max_heap_left or num <= -self.max_heap_left[0]:
            heappush(self.max_heap_left, -num)
        else:
            heappush(self.min_heap_right, num)

        # adjusting 
        if len(self.min_heap_right) > len(self.max_heap_left) + 1:
            smallest = heappop(self.min_heap_right)
            heappush(self.max_heap_left, -smallest)        
        elif len(self.max_heap_left) > len(self.min_heap_right) + 1:
            largest = -heappop(self.max_heap_left)
            heappush(self.min_heap_right, largest)

    def findMedian(self) -> float:
        if len(self.min_heap_right) > len(self.max_heap_left):
            return self.min_heap_right[0]
        elif len(self.max_heap_left) > len(self.min_heap_right):
            return -self.max_heap_left[0]
        else:
            return (-self.max_heap_left[0] + self.min_heap_right[0]) / 2     


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()