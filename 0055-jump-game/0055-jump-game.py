class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        end_ = 0
        for i in range(len(nums)):
            if i > end_:
                break 
            far = nums[i] + i 
            if far < end_:
                continue 
            else:
                end_ = far 
            
            
        return end_ >= len(nums) - 1

