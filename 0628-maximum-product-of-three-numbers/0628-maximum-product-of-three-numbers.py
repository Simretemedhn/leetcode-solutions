class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max_ = float("-inf")
        nums.sort()

        # the last 3 multiplication 
        max_ = max(max_, nums[-1] * nums[-2] * nums[-3])

        # the first 2 then the last one 
        max_ = max(max_, nums[0] * nums[1] * nums[-1])
        return max_