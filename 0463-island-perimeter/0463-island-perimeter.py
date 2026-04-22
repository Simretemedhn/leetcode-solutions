class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        visited = set()
        perimeter = 0
        
        def dfs(row, col):
            nonlocal perimeter
            
            visited.add((row, col))
            
            for dr, dc in direction:
                new_row = row + dr
                new_col = col + dc
                
                if not inbound(new_row, new_col) or grid[new_row][new_col] == 0:
                    perimeter += 1
                elif (new_row, new_col) not in visited:
                    dfs(new_row, new_col)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return perimeter  
        
        return perimeter 
            
