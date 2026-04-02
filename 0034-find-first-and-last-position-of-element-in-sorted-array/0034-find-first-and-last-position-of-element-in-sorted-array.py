from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        i = bisect_left(nums, target)
        if i < len(nums) and nums[i] == target:
            start = i
            j =  bisect_right(nums, target)
            end = j -1 
            return [start, end]
        else:
            return [-1, -1]

"""

    left = bisect_left(nums, target)
    right = bisect_right(nums, target) - 1
    
    if left <= right and left < len(nums) and nums[left] == target:
        return [left, right]
    else:
        return [-1, -1]
"""