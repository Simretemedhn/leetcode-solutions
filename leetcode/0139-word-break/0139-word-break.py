class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        memo = {}  
        
        def backtrack(start):
            if start in memo:
                return memo[start]
            
            if start == n:
                return True
            
            for end in range(start, n):
                word = s[start:end+1]
                if word in wordSet and backtrack(end+1):
                    memo[start] = True
                    return True
            
            memo[start] = False
            return False
        
        return backtrack(0)



"""class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        check = {False}
        def backtrack(start):
            if start == n:
                check.add(True)
                return 
            for end in range(start, n):
                word = s[start:end+1]
                if word in wordDict:
                    backtrack(end+1)
            return 
        return True in check """