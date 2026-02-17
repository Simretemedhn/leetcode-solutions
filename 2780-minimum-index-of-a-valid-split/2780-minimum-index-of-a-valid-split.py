from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)

        freq = Counter(nums)
        max_freq = max(freq.values())                
        dominant = [k for k, v in freq.items() if v == max_freq][0]  
        total_count = max_freq


        left_count = 0
        for i in range(n - 1):
            if nums[i] == dominant:
                left_count += 1
            
            left_size = i + 1
            right_size = n - left_size
            right_count = total_count - left_count
            
            if left_count * 2 > left_size and right_count * 2 > right_size:
                return i
        
        return -1
        