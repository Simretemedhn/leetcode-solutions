class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        place = row * col
        low = 0
        high = place - 1
        mid = (low + high)//2
        # row  = mid // col 
        # col = mid %  row 
        while low <= high:
            mid = (low + high)//2 
            new_row = mid//col 
            new_col = mid % col 

            if matrix[new_row][new_col] == target:
                return True 
            elif matrix[new_row][new_col] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False 
            
        