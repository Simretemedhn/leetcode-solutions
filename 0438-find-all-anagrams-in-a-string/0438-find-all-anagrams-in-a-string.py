from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        p_mapp = defaultdict(int)
        for letter in p:
            p_mapp[letter] += 1
        
        s_mapp = defaultdict(int)           
        for i in range(len(p)): 
            s_mapp[s[i]] += 1    
        
        result = []
        
        if s_mapp == p_mapp:   
            result.append(0)
        
        left = 0
        for right in range(len(p), len(s)):  
            s_mapp[s[right]] += 1
            
            s_mapp[s[left]] -= 1
            if s_mapp[s[left]] == 0:
                del s_mapp[s[left]]
            
            left += 1   
            
            if s_mapp == p_mapp:
                result.append(left)  
        
        return result
