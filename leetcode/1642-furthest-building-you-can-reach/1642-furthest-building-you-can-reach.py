from heapq import heappush, heappop
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        brick_climbs = []
        
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            
            if climb <= 0:
                continue
            
            heappush(brick_climbs, climb)
            
            if len(brick_climbs) > ladders:
                smallest_brick_climb = heappop(brick_climbs)
                bricks -= smallest_brick_climb
                
                if bricks < 0:
                    return i
        
        return len(heights) - 1