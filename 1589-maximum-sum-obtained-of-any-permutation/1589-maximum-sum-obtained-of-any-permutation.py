class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:    
        n = len(nums)
        MOD = 10**9 + 7
        
        freq = [0] * (n + 1) 
        
        for start, end in requests:
            freq[start] += 1
            freq[end + 1] -= 1
        
        for i in range(1, n):
            freq[i] += freq[i - 1]
        
        freq = sorted(freq[:-1], reverse=True)
        nums.sort(reverse=True)
        
        result = sum(num * f for num, f in zip(nums, freq) if f > 0) % MOD
        
        return result       
        