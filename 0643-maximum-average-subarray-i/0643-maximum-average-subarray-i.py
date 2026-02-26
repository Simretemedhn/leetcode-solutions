class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        max_sum = 0
        curr_sum  = 0
        while i < k:
            curr_sum += nums[i]
            i += 1
        max_sum = curr_sum
        j = 0
        for a in range(k, len(nums)):
            curr_sum += nums[a]
            curr_sum -= nums[j]
            j += 1
            max_sum = max(max_sum, curr_sum)
        return max_sum/k





        