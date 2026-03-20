from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(left, right):
            if left == right:
                return nums[left]
       
            pick_left = nums[left] - helper(left + 1, right)
            pick_right = nums[right] - helper(left, right - 1)

            return max(pick_left, pick_right)
        
        return helper(0, len(nums) - 1) >= 0



"""from collections import deque 
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        q = deque(nums)
        def select(q, score):
            if q[0] > q[-1]:
                score += q.popleft()
            else:
                score += q.pop()
        score_1 = 0
        score_2 = 0
        while q:
            select(q, score_1)
            if q: select(q, score_2)
        if score_1 >= score_2:
            return True 
        else:
            return False 
"""