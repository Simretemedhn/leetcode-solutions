from heapq import heappop, heapify, heappush
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        smallest = []

        for src, dst in points:
            distance = src*src + dst*dst
            heappush(smallest, (distance, src, dst))
        
        output = []
        for i in range(k):
            gap, src, dst = heappop(smallest)
            output.append([src, dst])

        return output 
