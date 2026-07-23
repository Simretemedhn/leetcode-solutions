class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        the_other_sum  = {}
        for i in range(len(nums)):
            the_other_sum[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in the_other_sum and the_other_sum[diff] != i:
                return [i, the_other_sum[diff]] 
    