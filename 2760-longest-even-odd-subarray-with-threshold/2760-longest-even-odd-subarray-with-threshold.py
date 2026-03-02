class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        left = -1
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                left = i
                break
        
        if left == -1:
            return 0
        
        max_len = 1
        right = left + 1
        
        while right < len(nums):
            valid = True
            
            if nums[right] > threshold:
                valid = False
            
            if valid and nums[right-1] % 2 == nums[right] % 2:
                valid = False
            
            if valid:
                max_len = max(max_len, right - left + 1)
                right += 1
            else: 
                left = right
                while left < len(nums) and (nums[left] % 2 != 0 or nums[left] > threshold):
                    left += 1
                
                if left >= len(nums):
                    break
                
                right = left + 1
                max_len = max(max_len, 1)
        
        return max_len
"""
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max_len = 0
        i = 0
        n = len(nums)
        
        while i < n:
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                j = i + 1
                while j < n and nums[j] <= threshold and nums[j-1] % 2 != nums[j] % 2:
                    j += 1
                max_len = max(max_len, j - i)
                i = j 
            else:
                i += 1
        
        return max_len

"""