class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        step = [0] * (n + 1) 
        
        for start, end, dire in shifts:
            if dire == 1:
                step[start] += 1
                step[end + 1] -= 1
            else:
                step[start] -= 1
                step[end + 1] += 1
        
        for i in range(1, n + 1):
            step[i] += step[i-1]
        
        result = []
        for i in range(n):
            shift = step[i] % 26  
            
            new_char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result) 

        