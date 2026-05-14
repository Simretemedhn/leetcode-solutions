from heapq import heappush, heappop

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        heap = []
        
        for j in range(min(k, len(nums2))):
            heappush(heap, (nums1[0] + nums2[j], 0, j))
        
        result = []
        
        while heap and len(result) < k:
            sum_val, i, j = heappop(heap)
            result.append([nums1[i], nums2[j]])
            
            if i + 1 < len(nums1):
                heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
        
        return result





# fist trial 
"""from heapq import heappush, heappop, heapify, heapreplace
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

            min_heap = []
            ind = 0
            while True:
                heappush(min_heap, (nums1[ind] + nums2[ind], ind, ind))
                heappush(min_heap, (nums1[ind+1] + nums2[ind], ind+1, ind))
                heappush(min_heap, (nums1[ind] + nums2[ind+1], ind, ind+1))

                if 2 * ind + 1 >= k:
                    break
                ind += 1  
            output = []
            for _ in range(k):
                sum_, i, j = min_heap[0]
                heappop(min_heap)
                output.append([nums1[i], nums2[j]])
            

            return output """