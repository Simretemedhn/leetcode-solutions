class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        changes = [0] * (len(s) + 1)
        
        for start, end, direction in shifts:
            if direction == 0:
                changes[start] -= 1 
                changes[end + 1] += 1 
            else:
                changes[start] += 1
                changes[end + 1] -= 1 
        
        for i in range(1, len(s) + 1):
            changes[i] += changes[i-1]
        
        result = []
        for i in range(len(s)):
            char = s[i]
            shift = changes[i] % 26  
            
            if 'a' <= char <= 'z':
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif 'A' <= char <= 'Z':
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                new_char = char
            result.append(new_char)
            
        return ''.join(result)
