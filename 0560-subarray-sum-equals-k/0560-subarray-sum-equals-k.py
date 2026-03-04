class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = {0:1}

        currSum = 0 
        for num in nums:
            currSum += num
            diff = currSum - k 
            res += prefix.get(diff, 0)
            prefix[currSum] = prefix.get(currSum, 0)  + 1

        return res 

        