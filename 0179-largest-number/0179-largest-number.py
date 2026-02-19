class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        new = list(map(str, nums))
        if sum(nums) == 0:
            return "0"
        for i in range(len(nums) - 1):
            for x in range(0, len(nums) - 1 - i):
                if new[x + 1] + new[x] > new[x] + new[x + 1]:
                    new[x + 1], new[x] = new[x], new[x + 1]
        return "".join(new)
