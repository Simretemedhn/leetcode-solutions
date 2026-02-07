class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = [num for num in nums if num < 10]
        double = [num for num in nums if num >= 10]

        return sum(single) != sum(double)
    