from heapq import heappush, heappop, heapify 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_heap = []

        for num in nums:
            if num != 0:
                heappush(max_heap, -num)
        
        largest = -heappop(max_heap)
        second_largest = -heappop(max_heap)

        return (largest - 1) * (second_largest - 1)
        