class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        prefix = {0:1}
        count = 0 

        current = 0 
        for i in range(len(nums)):
            current += nums[i]
            if current-goal in prefix:
                count += prefix[current-goal]
            prefix[current] = prefix.get(current, 0) + 1
        
        return count 
