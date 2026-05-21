from heapq import heappush, heappop, heapify
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []
        j = 0 
        for i in range(min(n, k)):
            for j in range(n):
                heappush(min_heap, matrix[i][j])

        min_val = 0
        for i in range(k):
            min_val = heappop(min_heap)
        return min_val 
