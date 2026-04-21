from bisect import bisect_left
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        for x in range(n + 1):
            pos = bisect_left(nums, x)
            count = n - pos  
            
            if count == x:
                return x
        
        return -1

