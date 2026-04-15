class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while i != nums[i]-1 and nums[nums[i]-1] != nums[i]: 
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        
        res = []
        for i in range(len(nums)):
            if nums[i]-1 != i:
                res.append(i+1) 
        return res

"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            while i != nums[i]-1 and nums[nums[i]-1] != nums[i]: 
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                print(nums)
        
        res = []
        for i in range(len(nums)):
            if nums[i]-1 != i:
                res.append(i+1) 
        return res 
"""   