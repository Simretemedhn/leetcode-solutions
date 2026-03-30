class Solution:
    def splitString(self, s: str) -> bool:
        
        def dfs(ind, prev):
            if ind >= len(s):
                return True 

            for j in range(ind, len(s)):
                val = int(s[ind:j+1]) 
                if val == prev - 1:
                    if dfs(j+1, val):  
                        return True
            return False  

        for i in range(len(s)-1):
            prev = int(s[:i+1])
            if dfs(i+1, prev):
                return True 
        return False