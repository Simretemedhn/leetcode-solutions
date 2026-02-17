class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for x in range(4):
            flag = True 
            for r in range(n):
                for c in range(n):
                    if x == 0:
                        if mat[r][c] != target[r][c]:
                            flag = False
                    elif x == 1:
                        if mat[r][c] != target[c][n-1-r]:
                            flag = False 
                    elif x == 2:
                        if mat[r][c] != target[n-1-r][n-1-c]:
                            flag = False
                    else:
                        if mat[r][c] != target[n-1-c][r]:
                            flag = False
                        
            if flag:
                return True 
        return False 
