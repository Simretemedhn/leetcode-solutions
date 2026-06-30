from collections import defaultdict 
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_one = sorted(nums)
        return [sorted_one.index(nums[i]) for i in range(len(nums))]

