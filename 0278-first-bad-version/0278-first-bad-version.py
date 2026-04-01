# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n % 2 != 0:
            half = (n+1)//2 
        else:
            half = n//2 
        
        if isBadVersion(half):
            half += 1
            while isBadVersion(half):
                half += 1
            return half 
        
        else:
            while not isBadVersion(half):
                half -= 1
            return half + 1
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                # If mid is bad, first bad is at mid or before
                right = mid
            else:
                # If mid is good, first bad is after mid
                left = mid + 1
        
        return left
