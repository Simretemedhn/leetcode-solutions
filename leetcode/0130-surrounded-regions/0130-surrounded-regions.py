class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        def isBorder(row, col):
            return row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]) - 1
        
        def inbound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        global_visited = set() 
        
        def dfs(row, col, region_visited, safe_region):
            region_visited.add((row, col))
            
            if isBorder(row, col):
                safe_region[0] = True
            
            for r, c in direction:
                new_row = row + r 
                new_col = col + c 
                
                if inbound(new_row, new_col) and board[new_row][new_col] == 'O' and (new_row, new_col) not in region_visited:
                    dfs(new_row, new_col, region_visited, safe_region)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in global_visited:
                    region_visited = set()  
                    safe_region = [False] 
                    dfs(i, j, region_visited, safe_region)
                    
                    global_visited.update(region_visited)
                    
                    if not safe_region[0]:  
                        for r, c in region_visited:  
                            board[r][c] = 'X'

"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:

        
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def checkSafe(row, col):
            if row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]):
                return True 

        visited = set()
        def dfs(row, col, safe):
            visited.add((row, col))
            for r, c in direction:
                new_row = row + r 
                new_col = col + c 
                if checkSafe(new_row, new_col):
                    safe = True        
                if board[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                    dfs(new_row, new_col, safe)
            
            if not safe:
                for cell in visited:
                    r, c = cell
                    board[r][c] = "X"

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0 and (i, j) not in visited:
                    dfs(i, j) """