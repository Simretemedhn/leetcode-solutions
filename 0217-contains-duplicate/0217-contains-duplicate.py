class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for x in range(1, len(nums)):
            if nums[x-1] == nums[x]:
                return True 
        return False 


        