class Solution:
    def findValidPair(self, s: str) -> str:
        num_map = {}
        for digit in s:
            num_map[digit] = num_map.get(digit, 0) + 1
        
        for x in range(len(s)-1):
            if s[x] != s[x+1]:
                first = int(s[x])
                second = int(s[x+1])
                if (int(s[x]) == num_map[s[x]]) and (int(s[x+1]) == num_map[s[x+1]]):
                    return s[x] + s[x+1]
        return ""

   