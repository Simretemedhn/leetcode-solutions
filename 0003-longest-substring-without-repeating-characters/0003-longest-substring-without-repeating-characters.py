class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sliding_window = set()
        maxx = 0 
        left = 0

        for right in range(len(s)):

            while s[right] in sliding_window:
                sliding_window.remove(s[left])
                left += 1

            sliding_window.add(s[right])
            maxx = max(maxx, right - left + 1)
        return maxx
            
            

    
        