class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        m = len(nums2)

        loop_ = []
        compare_with = set()
        
        if n >= m:
            loop_ = nums2
            compare_with = set(nums1)
        else:
            loop_ = nums1
            compare_with = set(nums2)  

        for i in range(len(loop_)):
            if loop_[i] in compare_with:
                return loop_[i]
        return -1