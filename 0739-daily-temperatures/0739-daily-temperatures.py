class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        answer = [0] * n

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
        return answer

        