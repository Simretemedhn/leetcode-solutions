class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_ = 0
        if nums[0] == 0 and len(nums) == 1:
            return True 
        for i, num in enumerate(nums):
            max_ = max(max_, num+i)
            if max_ == i and num == 0:
                return False 
            if max_ >= len(nums)-1:
                return True 
        return False 

        