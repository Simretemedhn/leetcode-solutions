class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # stack
        # stay in the stack until a bigger element is found
        num_map = {n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in num_map:
                continue     
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    ind = num_map[nums2[i]]
                    res[ind] = nums2[j] 
                    break 
        return res 

        stack = []
        greater = defaultdict(lambda : -1)

        for num in nums2:
            while stack and stack[-1] < num:
                greater[stack.pop()] = num
            stack.append(num)
        
        return [greater[num] for num in nums1]