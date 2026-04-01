class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        def find_left(nums, target):
            left = 0 
            right = len(nums) - 1
            ind = -1 
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] == target:
                    ind = mid 
                    right = mid - 1 
                elif nums[mid] > target:
                    right  = mid - 1 
                else:
                    left = mid + 1 
            return ind 
        
        def find_right(nums, target):
            left = 0 
            right  = len(nums) - 1 
            ind = -1 

            while left <= right:
                mid  = left + (right - left) // 2 
                if nums[mid] == target:
                    ind = mid 
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1 
                else:
                    left = mid + 1 
            return ind 

        first  = find_left(nums, target)
        second = find_right(nums, target)
        return [first, second]

