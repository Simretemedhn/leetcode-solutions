class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def backtrack(index, current_sum, current):
            if current_sum == target:
                result.append(current[:])
                return
            
            if index >= len(candidates) or current_sum > target:
                return
            
            # EXCLUDE
            backtrack(index + 1, current_sum, current)
            
            # INCLUDE
            if current_sum + candidates[index] <= target:
                current.append(candidates[index])
                backtrack(index, current_sum + candidates[index], current)
                current.pop()
        
        backtrack(0, 0, [])
        return result