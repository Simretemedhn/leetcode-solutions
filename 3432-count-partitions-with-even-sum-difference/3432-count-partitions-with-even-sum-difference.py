class Solution:
    def countPartitions(self, nums: List[int]) -> int:

        new = [0] * len(nums)

        current = 0
        for i in range(len(nums)):
            current = current + nums[i] 
            new[i] = current      

        count = 0 
        for i in range(len(new)-1):
            if (2*new[i] - new[-1])%2 == 0:
                count += 1
        return count
        
        