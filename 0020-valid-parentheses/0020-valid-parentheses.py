class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for symbol in s:
            if symbol in pairs:  # Closing bracket
                if not stack or stack[-1] != pairs[symbol]:
                    return False
                stack.pop()
            else:  # Opening bracket
                stack.append(symbol)
        
        return not stack