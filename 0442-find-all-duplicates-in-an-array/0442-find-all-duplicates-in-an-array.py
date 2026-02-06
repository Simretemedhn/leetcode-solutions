class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []

        for num in nums:
            if num in freq:
                res.append(num)
            else:
                freq[num] = 1

        return res
  
        