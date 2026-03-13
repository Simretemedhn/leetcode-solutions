from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mapp = defaultdict(int)
        mapp[0] = 1  
        curr_sum = 0
        count = 0
        
        for num in nums:
            curr_sum += num
            remainder = curr_sum % k
            
            count += mapp[remainder]
            
            mapp[remainder] += 1
            
        return count

"""

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mapp = {}
        curr_sum = 0
        count = 0
        for num in nums:
            curr_sum += num
            if curr_sum%k ==0:
                count += 1
            for m in mapp:
                if m == curr_sum or abs(m-curr_sum)%k == 0:
                    count += mapp[m] 
            mapp[curr_sum] = mapp.get(curr_sum, 0) + 1
        return count  

"""
