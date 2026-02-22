from collections import Counter 
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:   
        t_sorted = sorted(t)
        s_sorted = sorted(s)

        for i in range(len(s_sorted)):
            if t_sorted[i] != s_sorted[i]:
                return t_sorted[i]
        return t_sorted[-1]


