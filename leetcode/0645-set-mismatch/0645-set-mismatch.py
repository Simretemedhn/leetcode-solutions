class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        
        while i < n:
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if i+1 != nums[i]:
                return [nums[i], i+1]
"""
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            while nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
                nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
    
        for i in range(len(nums)):
            if i+1 != nums[i]:
                return [nums[i], i+1]
"""