class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if grid[r][c] < 0:
                    count += 1
                else:
                    break
        return count