from math import ceil, floor
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        prev_last = nums[-1]
        for i in range(len(nums)-2, -1, -1):

            if nums[i] <= prev_last:
                prev_last = nums[i]
                continue 
            
            else:
                if nums[i]% prev_last == 0:
                    count += nums[i]//prev_last - 1
                else:
                    curr = nums[i]              
                    pieces = ceil(nums[i] / prev_last)
                    prev_last = floor(nums[i] / pieces)
                    count += pieces - 1
                       
        return count                    
