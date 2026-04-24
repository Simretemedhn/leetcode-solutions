class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()
        row = len(grid)
        col = len(grid[0])   

        def inbound(_row, _col):
            return 0 <= _row < row and 0 <= _col < col

        def dfs(row, col):
            visited.add((row, col))
            count = 1  
            
            for dr, dc in direction:
                new_row = row + dr
                new_col = col + dc
                if inbound(new_row, new_col) and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                    count += dfs(new_row, new_col)            
            
            return count 
        
        max_area = 0 
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in visited:  
                    curr = dfs(r, c)
                    max_area = max(max_area, curr)  
        
        return max_area