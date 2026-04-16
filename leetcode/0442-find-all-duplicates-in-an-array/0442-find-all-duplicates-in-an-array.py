class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        i = 0
        while i < n:
            correct_pos = nums[i] - 1
            if nums[i] != i + 1 and nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1
        
        res = []
        for i in range(n):
            if nums[i] != i + 1:
                res.append(nums[i])
        
        return res
