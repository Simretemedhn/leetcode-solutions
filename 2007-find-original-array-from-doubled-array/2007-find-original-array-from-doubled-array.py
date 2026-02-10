from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        
        count = Counter(changed)
        sorted_keys = sorted(count.keys())
        original = []
        
        for x in sorted_keys:
            if count[x] > count[x * 2]:
                return []
            
            if x == 0:
                if count[x] % 2 != 0:
                    return []
                original.extend([0] * (count[x] // 2))
            else:
                original.extend([x] * count[x])
                count[x * 2] -= count[x]
                
        return original if len(original) == len(changed) // 2 else []