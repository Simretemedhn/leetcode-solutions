class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == "]":
                repeat = []
                while stack and stack[-1] != "[":
                    repeat.append(stack.pop())
                repeat = ''.join(reversed(repeat))
                
                stack.pop()  # remove '['
                
                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                num = int(''.join(reversed(num)))
                
                stack.append(repeat * num)  # More efficient
            else:
                stack.append(char)
        
        return ''.join(stack)
