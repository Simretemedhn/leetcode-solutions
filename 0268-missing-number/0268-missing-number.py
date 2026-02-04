class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        for x in range(len(nums)):
            if x not in nums:
                return x
        return x+1

        