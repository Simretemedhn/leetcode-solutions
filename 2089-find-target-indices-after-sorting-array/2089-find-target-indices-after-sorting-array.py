class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # using counting method 
        array = [0] * 101
        for num in nums:
            array[num] += 1 
        
        so_far_counted = 0
        for ind, freq in enumerate(array):
            if ind == target:
                result = []
                for f in range(freq):
                    result.append(so_far_counted)
                    so_far_counted += 1 
                return result 
            so_far_counted += freq 
            