class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(left, right):
            if left > right:
                return -1 
            mid = (left + right)//2 
            if nums[mid] > target:
                return helper(left, mid-1)
            elif nums[mid] < target:
                return helper(mid+1, right)
            else:
                return mid 
        return helper(0, len(nums)-1)