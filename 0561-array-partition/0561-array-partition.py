class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)%2 == 0:
            i = 0
        else:
            i = 1
        total = 0
        for j in range(i, len(nums), 2):
            total += nums[j]
        return total 

        

        