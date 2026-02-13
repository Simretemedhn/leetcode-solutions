from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        new_s = s.split(" ")
        pattern_map = defaultdict(list)
        s_map = defaultdict(list)
        for x in range(len(pattern)):
            pattern_map[pattern[x]].append(x)

        for y in range(len(new_s)):
            s_map[new_s[y]].append(y)

        return sorted(pattern_map.values()) == sorted(s_map.values())

        