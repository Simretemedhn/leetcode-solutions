class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # counting sort 
        write  = 0 
        for read in range(len(nums)):
            if nums[read] == 0:
                nums[read], nums[write] = nums[write], nums[read]
                write += 1 
        for read in range(len(nums)):
            if nums[read] == 1:
                nums[read], nums[write] = nums[write], nums[read]
                write += 1 
        for read in range(len(nums)):
            if nums[read] == 2:
                nums[read], nums[write] = nums[write], nums[read]
                write += 1       
        