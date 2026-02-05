class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        out = []
        for x in range(len(nums)):
            if nums[x] == target and not out:
                out.append(x)
                out.append(x)
            elif nums[x] == target:
                out[1] += 1
        return out if out else [-1, -1]
        