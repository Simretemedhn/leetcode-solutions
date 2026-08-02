class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtracking(start):
            if sum(path) == target:
                res.append(path[::])
                return 
            if sum(path) > target:
                return  #prunning 
            for i in range(start, len(candidates)):
                if sum(path) + candidates[i] > target:
                    break

                path.append(candidates[i])
                backtracking(i)
                path.pop()
        candidates.sort()
        backtracking(0)
        return res 
