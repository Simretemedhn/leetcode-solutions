class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_ = 0 

        for i in range(len(heights)):
            curr = heights[i]
            next_ind = i
            while stack and heights[stack[-1][0]] >= curr:  
                ind, starting_ind = stack.pop()
                max_ = max(max_, heights[ind] * (i - starting_ind))
                next_ind = starting_ind 
            stack.append((i, next_ind))
        
        while stack:
            ind, starting_ind = stack.pop()
            max_ = max(max_, heights[ind] * (len(heights) - starting_ind))
        
        return max_