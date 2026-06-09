from heapq import heappush, heappop

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Min-heap by capital requirement
        min_heap = []
        for i in range(len(capital)):
            heappush(min_heap, (capital[i], i))
        
        # Max-heap for profits of affordable projects
        max_heap = []
        
        for _ in range(k):
            # Add all projects we can afford to max_heap
            while min_heap and min_heap[0][0] <= w:  #  Check top, don't pop yet
                cap, idx = heappop(min_heap)  #  Now pop since we can afford
                heappush(max_heap, -profits[idx])
            
            # If no affordable projects, break
            if not max_heap:
                break
            
            # Take the most profitable project
            w += -heappop(max_heap)
        
        return w
