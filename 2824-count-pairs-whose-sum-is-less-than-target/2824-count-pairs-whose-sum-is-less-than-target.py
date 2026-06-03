class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        start = 0 
        end = len(nums) - 1 
        total = 0 

        while start <= end:

            if nums[start] + nums[end] < target:
                total += end - start 
                start += 1 
            else:
                end -= 1 
        return total 
