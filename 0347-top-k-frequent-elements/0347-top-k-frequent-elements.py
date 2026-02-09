from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        
        for _ in range(k):                
            max_val = max(count.values())
            
            keys_to_remove = []
            for key, value in count.items():
                if value == max_val:
                    res.append(key)
                    keys_to_remove.append(key)
                    
                    if len(res) == k:
                        break
            
            for key in keys_to_remove:
                count.pop(key)
            
            if len(res) == k:
                break
        
        return res
        