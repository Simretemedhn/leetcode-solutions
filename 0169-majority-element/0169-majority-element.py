from collections import Counter 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority = n // 2 
        for num, freq in Counter(nums).items():
            if freq > majority:
                return num 
