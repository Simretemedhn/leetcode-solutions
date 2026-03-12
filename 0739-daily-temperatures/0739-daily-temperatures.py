class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        stack_n = []
        stack_i = []
        res = [0] * len(nums)

        for i, n in enumerate(nums):
            while stack_n and stack_n[-1] < n:
                val = stack_n.pop()
                ind = stack_i.pop()
                res[ind] = i-ind 
            stack_n.append(n)
            stack_i.append(i) 
        return res 









        stack = []
        n = len(nums)
        answer = [0] * n

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
        return answer 