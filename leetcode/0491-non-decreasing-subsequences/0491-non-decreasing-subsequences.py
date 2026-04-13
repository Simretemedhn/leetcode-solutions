class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        def helper(ind, prev, path, res):
            if len(path) >= 2:
                res.append(path[::])
            if ind >= len(nums):  
                return 
            
            used = set() 
            for i in range(ind, len(nums)):
                if prev <= nums[i] and nums[i] not in used: 
                    used.add(nums[i])  
                    path.append(nums[i])
                    helper(i + 1, nums[i], path, res)
                    path.pop()

            return res 
        return helper(0, -101, [], [])
        
""" first trial 
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        def helper(ind, prev, path,  res):
            if len(path) >= 2:
                res.append(path[::])
            if ind >= len(nums) - 1:
                return 
            
            for i in range(ind, len(nums)):
                if prev <= nums[i]:
                    path.append(nums[i])
                    helper(i + 1, nums[i], path, res)
                    path.pop()

            return res 
        return helper(0, -101, [], [])

"""