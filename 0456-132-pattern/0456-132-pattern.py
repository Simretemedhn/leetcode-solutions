class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        stack = []
        min_left = nums[0]
        
        for num in nums[1:]:
            # Pop smaller elements
            while stack and stack[-1][0] < num:
                stack.pop()
            
            # Check if current num is the "2" between min_left and top
            if stack and stack[-1][1] < num < stack[-1][0]:
                return True
            
            # Update min_left and push current
            min_left = min(min_left, num)
            stack.append([num, min_left])
        
        return False