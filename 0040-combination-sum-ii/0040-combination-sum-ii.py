class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(start):
            if sum(sol) == target:
                res.append(sol[::])
                return 
            
            if sum(sol) > target:
                return 
            
            for i in range(start, len(candidates)):
                if sum(path) + candidates[i] > target:
                    break 
                path.append(candidates[i])
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        return res 


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sol = [] 
        candidates.sort()  
        
        def backtrack(start: int):
            if sum(sol) == target:
                res.append(sol[::])
                return
            
            if sum(sol) > target:
                return
            
            for i in range(start, len(candidates)):
                if sum(sol) + candidates[i] > target:
                    break
                
                # Skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                sol.append(candidates[i])
                backtrack(i + 1)
                sol.pop()
        
        backtrack(0)
        return res