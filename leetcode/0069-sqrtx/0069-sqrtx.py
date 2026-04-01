class Solution:
    def mySqrt(self, x: int) -> int:

        left = 1 
        right = x 
        res = 0

        while left <= right:
            mid = (left + right)//2 
            if mid * mid > x:
                right = mid - 1 
            elif mid * mid < x:
                res = mid
                left = mid + 1 
            else:
                res = mid
                break 
        return res 
