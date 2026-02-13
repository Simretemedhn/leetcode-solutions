from collections import Counter 

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        mag = Counter(magazine)

        for letter, freq in ransom.items():
            if mag[letter] < freq:
                return False 
        return True 
        