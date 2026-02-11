class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()
        arr = []
        maximum = 0
        for num in nums:
            if arr:
                if (num - arr[-1]) <= 1:
                    arr.append(num)
                else:
                    maximum = max(maximum, len(set(arr)))
                    arr = [num]  
            else:
                arr.append(num)
        
        maximum = max(maximum, len(set(arr)))
        return maximum