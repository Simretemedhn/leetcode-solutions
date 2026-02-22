class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_ = Counter(nums1)
        nums2_ = Counter(nums2)

        output = []
        for num, freq in nums1_.items():
            if num in nums2_:
                output.extend([num] * min(freq, nums2_[num]))
        return output

