class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        result = [-1] * len(nums1)


        mapp = {num: i for i, num in enumerate(nums1)}

        # building decreasing stack for nnum2 
        stack = []
        for i in range(n-1, -1, -1):

            while stack and stack[-1] < nums2[i]:
                stack.pop()
            if nums2[i] in mapp:
                index = mapp[nums2[i]]
                if stack:
                    result[index] = stack[-1] 

            stack.append(nums2[i])
        return result 

"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapp = {num: i for i, num in enumerate(nums1)}
        result = [-1] * len(nums1)
        stack = []  
        
        for i in range(len(nums2) - 1, -1, -1):
            current = nums2[i]
            
            # Remove elements that are smaller than current
            while stack and stack[-1] < current:
                stack.pop()
            
            # If current is in nums1, its next greater is stack[-1]
            if current in mapp:
                index = mapp[current]
                result[index] = stack[-1] if stack else -1
            
            # Push current onto stack
            stack.append(current)
        
        return result"""