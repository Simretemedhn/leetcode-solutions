from collections import defaultdict, Counter 
class Solution:
    def findLHS(self, nums: List[int]) -> int:

        c = defaultdict(int)

        for num in nums:
            c[(num, num+1)] += 1
            c[(num-1, num)] += 1

        Set = set(nums)

        output = 0
        for k, v in c.items():
            if k[0] in Set and k[1] in Set:
                output = max(output, v)

        return output 

        
