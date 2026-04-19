class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()

        result = 0 
        for i in range(1, len(nums)):
            result = max(result, nums[i]-nums[i-1])

        return result 