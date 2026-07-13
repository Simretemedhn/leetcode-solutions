class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        
        # Next smaller (right side)
        next_smaller = []
        nextt = [n] * n 
        for i in range(n):
            curr = heights[i]
            while next_smaller and heights[next_smaller[-1]] > curr:
                ind = next_smaller.pop()
                nextt[ind] = i 
            next_smaller.append(i)
        
        # Previous smaller (left side)
        prev_smaller = []
        prev = [-1] * n  
        for i in range(n):
            curr = heights[i]
            while prev_smaller and heights[prev_smaller[-1]] > curr:
                prev_smaller.pop()
            
            if prev_smaller:
                prev[i] = prev_smaller[-1]  
            prev_smaller.append(i)
        
        # Calculating max
        max_ = 0 
        for i in range(n):
            width = nextt[i] - prev[i] - 1 
            max_ = max(max_, heights[i] * width)
        return max_


""" first trial 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # we need both next smaller and previous smaller stack of indices 
        n = len(heights)
        next_smaller = []
        nextt = [n-1-i for i in range(n)]
        for i in range(n):
            curr = heights[i]
            while next_smaller and heights[next_smaller[-1]] > curr:
                ind = next_smaller.pop()
                nextt[ind] = i - ind - 1 
            next_smaller.append(i)
        
        prev_smaller = []
        prev = [i for i in range(n)]
        for i in range(n):
            curr = heights[i]
            while prev_smaller and heights[prev_smaller[-1]] > curr:
                prev_smaller.pop()
            
            if prev_smaller:
                ind = prev_smaller.pop()
                prev[ind] = i - ind - 1  
            prev_smaller.append(i)
        
        # calculating max from (next_Smaller, prev smaller and also itself, we use + 1 to indicate this)
        max_ = 0 
        for i in range(n):
            distance = prev[i] + nextt[i] + 1
            max_ = max(max_, heights[i] * distance)
        return max_"""


