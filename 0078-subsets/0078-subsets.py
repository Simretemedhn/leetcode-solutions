class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    
        def backtrack(start, curr_state):
            result.append(curr_state[:])

            for i in range(start, len(nums)):
                curr_state.append(nums[i])

                backtrack(i+1, curr_state)

                curr_state.pop()
                
        result = []
        backtrack(0, [])
        return result 