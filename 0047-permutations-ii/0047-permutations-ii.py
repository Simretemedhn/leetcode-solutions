class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, perm = [], []
        count = {n:0 for n in nums}

        for num in nums:
            count[num] += 1 
        
        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return 
            
            for c in count:
                if count[c] > 0:
                    perm.append(c)
                    count[c] -= 1 

                    dfs()

                    count[c] += 1 
                    perm.pop() 
        dfs()
        return res 
