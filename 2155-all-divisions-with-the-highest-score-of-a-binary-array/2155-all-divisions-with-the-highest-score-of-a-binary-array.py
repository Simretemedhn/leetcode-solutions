from collections import defaultdict
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        #starting count when numsleft is empty and nums right is full 
        score = 0 
        for num in nums:
            if num == 1:
                score += 1 
        indice_map_to_score = defaultdict(list)
        indice_map_to_score[score] = [0]
        # then everytime we encounter 0 we add to the score ans 
        # and everytime we encounter 1 we substract 1 from the score 

        for ind in range(1, len(nums)+1):
            if nums[ind-1] == 0:
                score += 1 
            else:
                score -= 1 
            indice_map_to_score[score].append(ind)
        return indice_map_to_score[max(indice_map_to_score)]

