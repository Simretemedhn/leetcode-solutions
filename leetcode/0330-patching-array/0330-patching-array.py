class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        total =  0
        i = 0
        cover = 0
        total = 0
        patch = 0
        while total < n:
            if total > cover:
                cover = total
            if i < len(nums) and cover+1 == nums[i]:
                cover += 1
                total += nums[i]
                i += 1 
            
            elif i < len(nums) and cover+1 > nums[i]:
                total += nums[i]
                i += 1

            else:
                patch += 1
                cover += 1
                total += cover
        return patch 