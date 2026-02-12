class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        char_map1 = {}
        char_map2 = {}

        for char1 in word1:
            char_map1[char1] = char_map1.get(char1, 0) + 1
        for char2 in word2:
            char_map2[char2] = char_map2.get(char2, 0) + 1

        if (sorted(char_map1) == sorted(char_map2)) and (sorted(char_map1.values()) == sorted(char_map2.values())):
            return True 
        else:
            return False 
        