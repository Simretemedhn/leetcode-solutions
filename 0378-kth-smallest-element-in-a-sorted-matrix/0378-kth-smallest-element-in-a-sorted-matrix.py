from heapq import heappush, heappop, heapify
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []

        for i in range(min(n, k)):
            heappush(min_heap, (matrix[i][0], i, 0))

        for _ in range(k-1):
            val, row, col = heappop(min_heap)

            if col + 1 < n:
                heappush(min_heap, (matrix[row][col + 1], row, col + 1))
        return min_heap[0][0]

