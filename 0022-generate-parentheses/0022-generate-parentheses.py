class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(used_opening, used_closing, path):
            if used_opening == n and used_closing == n:
                res.append("".join(path))
                return 
            
            if used_opening < n:
                path.append("(")
                backtracking(used_opening+ 1, used_closing, path)
                path.pop()
            if used_closing < used_opening:
                path.append(")")
                backtracking(used_opening, used_closing + 1, path)
                path.pop()

        backtracking(0, 0, [])
        return res 
