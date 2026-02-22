from collections import Counter 
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:   
        t_map = Counter(t)

        for char in s:
            t_map[char] -= 1

        for char, freq in t_map.items():
            if freq == 1:
                return char 

