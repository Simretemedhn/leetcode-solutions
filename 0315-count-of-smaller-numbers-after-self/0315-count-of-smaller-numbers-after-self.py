from bisect import bisect_left, bisect_right  
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        collec = []
        sorting = []
        def finding_postition_to_put_on(num):
            nonlocal collec
            pos = bisect_left(sorting, num)
            collec.append(pos)
            sorting.insert(pos, num)


        n = len(nums)
        for i in range(n-1, -1, -1):
            finding_postition_to_put_on(nums[i])
        return collec[::-1]

        