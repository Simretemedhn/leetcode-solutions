
from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_count = Counter(s)
        result = []
        for x in order:
            if x in s_count:
                result.append(x * s_count[x])
                s_count.pop(x)
        for y in s_count:
            result.append(y * s_count[y])
        return "".join(result)