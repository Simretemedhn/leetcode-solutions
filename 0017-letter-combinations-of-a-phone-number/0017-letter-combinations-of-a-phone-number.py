class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        result, path = [], []
        def backtrack(i):
            if i == len(digits):
                result.append("".join(path))
                return 
            
            letters = phone_map[digits[i]]
            for letter in letters:
                path.append(letter)
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        return result