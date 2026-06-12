import heapq
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_heap = []
        for c in candies:
            heapq.heappush(max_heap, -c)
        
        max_candies = -max_heap[0]  
        
        result = []
        for c in candies:
            result.append(c + extraCandies >= max_candies)
        
        return result