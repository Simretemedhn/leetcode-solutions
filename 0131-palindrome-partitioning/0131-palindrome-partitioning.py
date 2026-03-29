class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current = []
        
        def backtrack(start):
            if start == len(s):
                result.append(current[:])  
                return
            
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                if substring == substring[::-1]:
                    current.append(substring)
                    backtrack(end)
                    current.pop() 
        
        backtrack(0)
        return result


        