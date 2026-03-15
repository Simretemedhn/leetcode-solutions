from collections import defaultdict 
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt = defaultdict(int)
        for bill in bills:
            if bill == 5:
                cnt[5] += 1
                continue 
            elif bill == 10 and cnt[5] > 0:
                cnt[5] -= 1
            elif bill == 20 and cnt[10] > 0 and cnt[5] > 0:
                cnt[10] -= 1
                cnt[5] -= 1
            elif bill == 20 and cnt[5] >=3:
                cnt[5] -= 3
            else:
                return False 
            cnt[bill] += 1
        return True 
        