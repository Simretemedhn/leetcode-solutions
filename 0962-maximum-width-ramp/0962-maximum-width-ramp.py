class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        width = 0
        stack = []

        # decreasing stack 
        for i in range(len(nums)):
            curr = nums[i]

            if not stack or nums[stack[-1]] >  curr:
                stack.append(i)
        for i in range(len(nums)-1, -1, -1):
            curr = nums[i]
            while stack and nums[stack[-1]] <= curr:
                ind = stack.pop() 
                width = max(width, i - ind)
        return width 


