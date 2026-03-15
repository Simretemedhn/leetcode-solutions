from math import ceil 
from collections import Counter 
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answer_map = Counter(answers)
        count = 0
        for key, value in answer_map.items():
            if key == 0:
                count += value
            elif key+1 <value:
                segments = ceil(value/(key+1))
                count += ((key+1) * segments)
            
            else:
                count += (key+1)
        return count 



        