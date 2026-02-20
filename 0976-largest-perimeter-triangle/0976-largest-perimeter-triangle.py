class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        a = -3
        b = -2
        c = -1
        for i in range(len(nums)-2):
            if nums[a] + nums[b] > nums[c]:
                return nums[a] + nums[b] + nums[c]
            else:
                a -= 1
                b -= 1
                c -= 1
        return 0


        