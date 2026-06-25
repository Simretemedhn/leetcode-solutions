class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for operation in range(len(nums)-1):
            if nums[operation] == nums[operation + 1]:
                nums[operation] *= 2 
                nums[operation + 1] = 0
        
        write = 0 
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[read], nums[write] = nums[write], nums[read]
                write += 1 
        return nums

            

        