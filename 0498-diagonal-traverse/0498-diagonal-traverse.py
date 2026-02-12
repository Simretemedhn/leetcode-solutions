class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        result = []
        
        for diagonal_sum in range(m + n - 1):
            if diagonal_sum % 2 == 0: 
                i = min(diagonal_sum, m - 1) 
                j = diagonal_sum - i  
                while i >= 0 and j < n:
                    result.append(mat[i][j])
                    i -= 1
                    j += 1
            else: 
              
                j = min(diagonal_sum, n - 1) 
                i = diagonal_sum - j  
                while j >= 0 and i < m:
                    result.append(mat[i][j])
                    i += 1
                    j -= 1
        
        return result



            
