from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque() 
        min_deque = deque()
        left = 0
        max_len = 0
        
        for right, num in enumerate(nums):
            while max_deque and num > nums[max_deque[-1]]:
                max_deque.pop()
            max_deque.append(right)
            
            while min_deque and num < nums[min_deque[-1]]:
                min_deque.pop()
            min_deque.append(right)
            
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                if max_deque[0] == left:
                    max_deque.popleft()
                if min_deque[0] == left:
                    min_deque.popleft()
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len