class Solution:
    def ispal(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False 
            i += 1
            j -= 1 
        return True 
    def partition(self, s: str) -> List[List[str]]:
        res, curr = [], []

        def backtrack(start):
            if start == len(s):
                res.append(curr[:])
                return 
            
            for j in range(start, len(s)):
                if self.ispal(s, start, j):
                    curr.append(s[start:j+1])
                    backtrack(j+1)
                    curr.pop()
        backtrack(0)
        return res 
