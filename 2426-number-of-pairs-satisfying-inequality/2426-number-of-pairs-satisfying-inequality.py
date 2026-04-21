import bisect

class Solution:
    def numberOfPairs(self, nums1, nums2, diff):
        n = len(nums1)
        a = [nums1[i] - nums2[i] for i in range(n)]
        
        sorted_values = []
        count = 0
        
        for j in range(n):
            target = a[j] + diff
            pos = bisect.bisect_right(sorted_values, target)
            count += pos
            
            bisect.insort(sorted_values, a[j])
        
        return count
"""

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        gap = [nums1[i] - nums2[i] for i in range(n)]

        def binarySearch(num, arr):
            arr.sort()
            low = 0 
            high = len(arr) - 1 
            res = 0
            while low <= high:
                mid = (high + low)//2 
                if num - arr[mid] - diff <= 0:
                    res = i - mid 
                    high = mid - 1
                else:
                    low = mid + 1 
            return res


        count = 0
        for i in range(n-1, 0, -1):
            count += binarySearch(gap[i], gap[:i])
        return count 



        gap.sort()







        count = 0 
        for i in range(n-1, 0, -1):
            low = 0 
            high = i - 1 
            res = 0
            while low <= high:
                mid = (high + low)//2 
                if gap[i] - gap[mid] - diff <= 0:
                    res = i - mid 
                    high = mid - 1
                else:
                    low = mid + 1 
            count += res 
        return count  """



