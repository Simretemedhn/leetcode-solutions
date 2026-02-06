class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = Counter(nums)
        for each in x:
            if x[each] == 1:
                return each
        