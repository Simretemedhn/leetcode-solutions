class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Hashmap
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = ['']
        for digit in digits:
            letters = phone[digit]
            new_result = []
            for combo in result:
                for letter in letters:
                    new_result.append(combo + letter)
            result = new_result

        return result



