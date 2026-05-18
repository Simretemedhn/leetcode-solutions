from heapq import heappush, heappop
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_heap = []
        
        for i in range(1, len(heights)):
            gap = heights[i] - heights[i-1]
            
            if gap <= 0:
                continue
            
            heapq.heappush(ladder_heap, gap)
            
            if len(ladder_heap) > ladders:
                smallest_ladder_gap = heapq.heappop(ladder_heap)
                
                if bricks >= smallest_ladder_gap:
                    bricks -= smallest_ladder_gap
                else:
                    return i - 1
        
        return len(heights) - 1
        



# first trial 
"""from heapq import heappush, heappop, heapify 
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        gaps = []
        for i in range(1, len(heights)):
            if heights[i] > heights[i-1]:
                gaps.append(heights[i-1] - heights[i])

        heap_ladder = []
        heap_bricks = []
        for gap in gaps:
            if len(heap_ladder) < ladders:
                heapq.heappush(heap_ladder, gap)
            elif heap_ladder[0] < gap:
                # pop then add to the brick 
                # push this gap to the ladder then 
                remove = heapq.heappop(heap_ladder)
                heapq.heappush(heap_ladder, gap)
                if bricks + sum(heap_brick) >= remove:
                    heapq.heappush(-remove)
                     
                else:
                    break
            else:
                if bricks + sum(heap_brick)  >= gap:
                    heapq.heappush(-gap)
                else:
                    break """
  
