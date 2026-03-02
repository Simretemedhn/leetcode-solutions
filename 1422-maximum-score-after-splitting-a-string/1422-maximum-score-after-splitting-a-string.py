from collections import Counter 
class Solution:
    def maxScore(self, s: str) -> int:
        s_map = Counter(s)
        l_level = 0
        r_level = s_map["1"]
        max_score = 0

        for i in range(len(s)-1):
            if s[i] == "0":
                l_level += 1
            else:
                r_level -= 1
            max_score = max(max_score, l_level + r_level)
        return max_score 

