class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return int(n*(n+1)/2) - sum(nums)








        """nums = set(nums)
        for x in range(len(nums)):
            if x not in nums:
                return x
        return x+1 """

        