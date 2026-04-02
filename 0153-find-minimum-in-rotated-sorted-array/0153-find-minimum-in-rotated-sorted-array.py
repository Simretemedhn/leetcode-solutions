class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:  
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
""" first trial 
class Solution:
    def findMin(self, nums: List[int]) -> int:

        lowest = 0 
        highest = len(nums) - 1 

        while lowest <= highest:
            mid = (lowest + highest)//2 
            if nums[lowest] < nums[mid] and nums[mid] > nums[highest]:
                lowest = mid + 1 
            elif nums[lowest] > nums[mid] and nums[mid] < nums[highest]:
                highest = mid 
            elif nums[lowest] <= nums[mid] and nums[mid] <= nums[highest]:
                return nums[lowest]


"""
        
