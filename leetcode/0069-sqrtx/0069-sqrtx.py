class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        if x < 4: return 1 

        low = 2
        high = x//2
        res = 0

        while low <= high:
            mid = (low + high)//2 
            if mid * mid < x:
                res = mid
                low = mid + 1 
            elif mid * mid > x:
                high = mid -1 
            else:
                return mid 
        return res 
        
        