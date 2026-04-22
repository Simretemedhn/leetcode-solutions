class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        def dfs(row, col):
            visited.add((row, col))

            for dr, dc in direction:
                new_row = row + dr 
                new_col = col + dc 

                if inbound(new_row, new_col) and grid[new_row][new_col] == "1" and (new_row, new_col) not in visited:
                    dfs(new_row, new_col)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count  += 1 
                    dfs(i,j)

        return count 