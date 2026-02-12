class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for x in range(len(nums)-1):
            if nums[x] == nums[x+1]:
                nums[x] *= 2
                nums[x+1] = 0 

        new = [x for x in nums if x != 0]
        new.extend([0] * (len(nums)-len(new)) )
        return new