from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:

        sorted_nums = dict(sorted(Counter(nums).items()))

        firs_elem = min(nums)
        elems = []
        freqs = []
        max_ = 0
        for key,freq in sorted_nums.items():
            elems.append(key)
            freqs.append(freq)

        for i in range(1, len(set(nums))):
            if elems[i] - elems[i-1] == 1:
                max_ = max(max_, freqs[i] + freqs[i-1])  
        return max_ 

"""        
        count = 0
        left = 0
        for right in range(1, len(nums)):
            if nums[right]-nums[left] > 1:
                left += 1
            else:
"""



        