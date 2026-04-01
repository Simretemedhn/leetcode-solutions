
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowest = 1
        highest = max(piles)
        res = 0

        while lowest <= highest:
            mid = (lowest + highest) // 2

            count = 0
            for pile in piles:
                
                count += (pile + mid - 1) // mid
            
            if count > h:
                lowest = mid + 1 
            else:  
                res = mid 
                highest = mid - 1 
            
        return res

        