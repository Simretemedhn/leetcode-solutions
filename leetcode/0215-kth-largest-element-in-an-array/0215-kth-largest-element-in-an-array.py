from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heappush(min_heap, num)
            else:
                if min_heap[0] < num:  
                    heappop(min_heap)   
                    heappush(min_heap, num)  
        return min_heap[0]