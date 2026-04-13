class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        def helper(i, subseq):
            if i == len(nums):
                if len(subseq) >= 2:
                    self.res.add(tuple(subseq))
                return 
            
            if not subseq or subseq[-1] <= nums[i]:
                helper(i + 1, subseq + [nums[i]])
            
            helper(i+1, subseq)
        
        self.res = set()
        helper(0, [])
        return [list(x) for x in self.res]  