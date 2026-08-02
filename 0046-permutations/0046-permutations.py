class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)

        def backtrack(curr_state):
            if len(curr_state) == len(nums):
                result.append(curr_state[:])

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True 
                    curr_state.append(nums[i])
                    backtrack(curr_state)

                    used[i] = False 
                    curr_state.pop()
        result = [ ]
        backtrack([])
        return result 