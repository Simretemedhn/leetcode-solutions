from math import floor 
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        appear = floor(len(nums)/3)
        x = Counter(nums)
        for each in x:
            if x[each] >appear:
                result.append(each)
        return result 
        