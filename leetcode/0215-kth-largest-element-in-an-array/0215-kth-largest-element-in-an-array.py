class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def divide(arr, k):
            if len(arr) == 1:
                return arr[0]
            
            pivot = arr[0]
            
            left = [x for x in arr if x < pivot]
            mid = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            
            if k <= len(right):
                return divide(right, k)
            elif k <= len(right) + len(mid):
                return pivot
            else:
                return divide(left, k - len(right) - len(mid))
        
        return divide(nums, k)
"""class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # quick sort
        def divide(arr):
            if len(arr) <= 1:
                return arr[0]
            pivot = arr[0]

            l = [x for x in arr[1:] if x <= pivot]
            r = [x for x in arr[1:] if x > pivot]

            if k == len(r)+1:
                return pivot
            elif k <= len(r):
                return divide(r)
            else:
                return divide(l)
        return divide(nums)
"""