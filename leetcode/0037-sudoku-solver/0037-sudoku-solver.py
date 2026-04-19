class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(row, col, num_char):
            for c in range(9):
                if board[row][c] == num_char:
                    return False
            for r in range(9):
                if board[r][col] == num_char:
                    return False
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    if board[r][c] == num_char:
                        return False
            return True
        
        def solve():
            min_options = 10
            best_r, best_c = -1, -1
            
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        options = 0
                        for num in range(1, 10):
                            if isValid(r, c, str(num)):
                                options += 1
                        
                        if options < min_options:
                            min_options = options
                            best_r, best_c = r, c
                            
                            if min_options == 1:  
                                break
                if min_options == 1:
                    break
            
            if best_r == -1:  
                return True
            
            for num in range(1, 10):
                num_char = str(num)
                if isValid(best_r, best_c, num_char):
                    board[best_r][best_c] = num_char
                    if solve():
                        return True
                    board[best_r][best_c] = "."
            
            return False
        
        solve()