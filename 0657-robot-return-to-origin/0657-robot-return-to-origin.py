from collections import Counter
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count  = Counter(moves)


        if ("U" in count) != ("D" in count):
            return False 
        if "U" in count and count["U"] != count["D"]:
            return False 
        


        if ("L" in count) != ("R" in count):
            return False 
        if ("L" in count) and (count["L"] != count["R"]):
            return False 
        return True 