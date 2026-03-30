class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {"2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz",
                    "0": "-",
                    "*": "+",
                    "#": ""} 
        res, part = [], []

        def backtrack(i, part):
            if len(part) == len(digits):
                res.append(part[::])
                return 
            
            for c in phone_map[digits[i]]:
                backtrack(i+1, part+c)
        backtrack(0, "")

        return res 
    
