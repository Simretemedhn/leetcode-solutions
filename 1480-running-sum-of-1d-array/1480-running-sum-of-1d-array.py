class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        accumulator  = 0 
        running_sum = []

        for i in range(len(nums)):
            accumulator += nums[i]
            running_sum.append(accumulator)
        
        return running_sum