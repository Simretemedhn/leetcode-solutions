class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {}
        for ind, char in enumerate(s):
            last_occurrence[char] = ind
        
        result = []
        left = 0
        right = 0
        
        for i in range(len(s)):

            right = max(right, last_occurrence[s[i]])
            

            if i == right:
                result.append(right - left + 1)
                left = i + 1  
        return result