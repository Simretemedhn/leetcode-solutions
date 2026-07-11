class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        # Build increasing stack (monotonic)
        for digit in num:
            while stack and stack[-1] > digit and k > 0:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If k > 0, remove remaining digits from the end
        if k > 0:
            stack = stack[:-k]
        
        # Remove leading zeros 
        start = 0
        while start < len(stack) and stack[start] == '0':
            start += 1
        
        # If all digits are zeros or empty
        if start == len(stack):
            return "0"
        
        return ''.join(stack[start:])