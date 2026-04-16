class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        i = 0
        while i < n:
            correct_pos = nums[i] - 1
            if nums[i] != i + 1 and nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                return nums[i]
        
        return -1  


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] != i + 1:
                correct_pos = nums[i] - 1
                if nums[correct_pos] == nums[i]:
                    break
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]        
        for i in range(n):
            if nums[i] != i + 1:
                return nums[i]
        
        return -1

"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        for i in range(n):

            while nums[i] != i + 1 and nums[nums[i]-1] != nums[i]:
                nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i] 
                print(nums)
        for i in range(n):
            if nums[i] != i + 1:
                return nums[i]
"""