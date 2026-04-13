from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        starting_ind = bisect_left(nums, target)
        if starting_ind >= len(nums) or nums[starting_ind] != target:
            return [-1, -1]
        ending_ind = bisect_right(nums, target)
        return [starting_ind, ending_ind-1]

        