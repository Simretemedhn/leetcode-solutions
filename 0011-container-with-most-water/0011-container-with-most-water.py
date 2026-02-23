class Solution:
    def maxArea(self, height: List[int]) -> int:
  
        left, max_area, right = 0, 0, len(height) - 1   
        while left < right:
            h = min(height[right], height[left])
            w = right - left
            max_area = max(max_area, h * w)
            if height[right] <= height[left]:
                right -= 1
            else:
                left += 1
        return max_area 