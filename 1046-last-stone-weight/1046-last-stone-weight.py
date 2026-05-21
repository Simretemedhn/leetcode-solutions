from heapq import heappush, heappop, heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapify(max_heap)

        while len(max_heap) > 1:
            first_larger = -heappop(max_heap)
            second_larger = -heappop(max_heap)

            diff = first_larger - second_larger 
            if diff > 0:
                heappush(max_heap, -diff)
        
        return -max_heap[0] if len(max_heap) == 1 else 0 
         