class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0] * n
        pref[0] = nums[0] 
        for i in range(1, n):
            pref[i] = pref[i-1] + nums[i]
        return max(1, 1 - min(pref))
        