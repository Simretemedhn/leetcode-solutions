class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        collection = []
        visited = set()  
        
        def is_safe(row, col):
            for j in range(col):
                if (row, j) in visited:
                    return False
            
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if (i, j) in visited:
                    return False
                i -= 1
                j -= 1
            
            i, j = row + 1, col - 1
            while i < n and j >= 0:
                if (i, j) in visited:
                    return False
                i += 1
                j -= 1
            
            return True
        
        def backtrack(col):
            if col == n:
                board = [['.' for _ in range(n)] for _ in range(n)]
                for r, c in visited:
                    board[r][c] = 'Q'
                collection.append([''.join(row) for row in board])
                return
            
            for row in range(n):
                if is_safe(row, col):
                    visited.add((row, col))
                    backtrack(col + 1)
                    visited.remove((row, col))
        
        backtrack(0)
        return collection