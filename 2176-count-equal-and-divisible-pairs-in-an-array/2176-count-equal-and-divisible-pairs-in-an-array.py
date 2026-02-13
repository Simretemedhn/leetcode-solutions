from collections import defaultdict 
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        map_ind = defaultdict(list)
        for x in range(len(nums)):
            map_ind[nums[x]].append(x)
        count = 0
        for key, indices in map_ind.items():

            for i in range(len(indices)):
                for j in range(i + 1, len(indices)):
                    if (indices[i] * indices[j]) % k == 0:
                        count += 1
        return count


        