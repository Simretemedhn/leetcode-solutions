class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # the first sliding window 
        n = len(nums)
        total = 0 
        for i in range(k):
            total += nums[i]
        max_sum = total  

        left = 0 
        for right in range(k, n):
            # next window will be adding the element in the right position and removing the element in the left position then incrementing 
            total += nums[right]
            total -= nums[left]
            left += 1 

            max_sum = max(max_sum, total)
        
        return max_sum/k