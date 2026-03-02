class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        
        nums = [int(ch) for ch in s]
        
        prefix_ones = [0] * n
        prefix_ones[0] = nums[0]
        for i in range(1, n):
            prefix_ones[i] = prefix_ones[i-1] + nums[i]
        
        total_ones = prefix_ones[-1]
        max_score = 0
        
        for i in range(n-1): 
            zeros_in_left = (i + 1) - prefix_ones[i]
            ones_in_right = total_ones - prefix_ones[i]
            
            score = zeros_in_left + ones_in_right
            max_score = max(max_score, score)
        
        return max_score

