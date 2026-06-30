from collections import defaultdict 
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        # elements which are already in arr2 
        # counting is best 

        mapp = defaultdict(int)
        arr2_set = set(arr2)
        not_in_arr2 = []
        for num in arr1:
            if num in arr2_set:
                mapp[num] += 1
            else:
                not_in_arr2.append(num)
        result = []
        for num in arr2:
            result.extend([num] * mapp[num]) 
        not_in_arr2.sort()
        
        return result + not_in_arr2


