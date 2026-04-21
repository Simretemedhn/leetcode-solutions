from collections import defaultdict
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def findones(arr):
            low = 0
            high = len(arr)-1 
            res = 0
            while low <= high:
                mid = (low + high)//2 
                if arr[mid] == 0:
                    high = mid - 1
                else:
                    res = mid + 1 
                    low = mid + 1 
            return res 
        
        mapp = defaultdict(list)
        for i in range(len(mat)):
            matrix = mat[i]
            ones = findones(matrix) 
            mapp[ones].append(i)
        sorted_map = dict(sorted(mapp.items()))

        result = []
        for solider, indexes in sorted_map.items():
            if len(indexes) > 1:
                indexes.sort()
            result.extend(indexes)
        return result[:k] 