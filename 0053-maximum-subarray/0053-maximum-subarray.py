
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        accu = 0 

        for num in nums:
            accu += num
            max_sum = max(max_sum, accu)  
            if accu < 0:                   
                accu = 0                   
        return max_sum
