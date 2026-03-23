class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_q = deque()  
        output = []
        
        for i in range(k):
            while max_q and nums[max_q[-1]] < nums[i]:
                max_q.pop()
            max_q.append(i) 
        output.append(nums[max_q[0]]) 
        
        for i in range(k, len(nums)):
            if max_q and max_q[0] == i - k:
                max_q.popleft()
            
            while max_q and nums[max_q[-1]] < nums[i]:
                max_q.pop()
            max_q.append(i)
            
            output.append(nums[max_q[0]])
        
        return output