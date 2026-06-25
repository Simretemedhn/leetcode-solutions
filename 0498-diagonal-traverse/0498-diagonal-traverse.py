from collections import defaultdict 
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal_sum_map_to_values  = defaultdict(list)

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                diagonal_sum_map_to_values[row + col].append(mat[row][col])
        
        result = []
        for sum_ in diagonal_sum_map_to_values:
            if sum_ % 2 == 0:
                diagonal_sum_map_to_values[sum_].reverse()
            result.extend(diagonal_sum_map_to_values[sum_])
        return result 

