class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        path = set() 

        def check(r, c, i):
            if i == len(word):
                return True 
            if r < 0 or c < 0 or r >= row or c >= col or board[r][c] != word[i] or (r, c) in path:
                return False 
            
            path.add((r, c))
            if (check(r + 1, c, i + 1) or 
                check(r - 1, c, i + 1) or 
                check(r, c + 1, i + 1) or 
                check(r, c - 1, i + 1)):
                return True 
            path.remove((r, c))
            return False  

        for i in range(row):
            for j in range(col):
                if check(i, j, 0):  
                    return True 
                
        return False