class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = 0
        
        while low <= high:
            mid = (low + high)//2 

            count = 0 
            for pile in piles:
                count += (pile + mid - 1)//mid   #ceiling 
            if count > h:
                low = mid + 1 
            else:
                res = mid 
                high = mid - 1 
        return res 