from collections import Counter
class Solution:
    def findValidPair(self, s: str) -> str:
        num_map = Counter(s)

        for x in range(len(s)-1):
            if s[x] != s[x+1]:
                if (int(s[x]) == num_map[s[x]]) and (int(s[x+1]) == num_map[s[x+1]]):
                    return s[x] + s[x+1]
        return ""


   