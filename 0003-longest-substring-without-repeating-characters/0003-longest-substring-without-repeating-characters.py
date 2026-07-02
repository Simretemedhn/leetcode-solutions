class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0 
        mapp = {}
        max_len = 0 
        for right in range(len(s)):
            
            while s[right] in mapp:
                # we have to shrink 

                mapp[s[left]] -= 1 
                if mapp[s[left]] == 0:
                    del mapp[s[left]]
                left += 1 
            mapp[s[right]] = 1
            max_len = max(max_len, right - left + 1)
        return max_len
        