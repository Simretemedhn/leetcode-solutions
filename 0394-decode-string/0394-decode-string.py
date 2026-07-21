class Solution:
    def decodeString(self, s: str) -> str:
        def helper(i):
            result = ""
            num = 0
            
            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                elif s[i] == '[':
                    # Recursively decode the inner string
                    substring, i = helper(i + 1)
                    result += num * substring
                    num = 0  # Reset num for next encoding
                elif s[i] == ']':
                    return result, i
                else:
                    result += s[i]
                i += 1
            
            return result
        
        return helper(0)      