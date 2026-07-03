class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        accum = 0 
        count = 0
        for i in range(len(nums)):
            accum += nums[i]
            if accum - k in dic:
                count += dic[accum - k]
            dic[accum] = dic.get(accum, 0) + 1
        return count 


