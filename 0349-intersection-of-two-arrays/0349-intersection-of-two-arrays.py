class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_1 = set(nums1)
        num_2 = set(nums2)
        
        output = []
        for num in num_1:
            if num in num_2:
                output.append(num)
        return output