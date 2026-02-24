class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        output = ""
        
        for word in dictionary:
            i = 0 
            j = 0  
            
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1  
                i += 1  
            
            if j == len(word):
                if len(word) > len(output):
                    output = word
                elif len(word) == len(output) and word < output:
                    output = word
        
        return output