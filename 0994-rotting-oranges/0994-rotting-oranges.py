class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh = 0
        q = deque()
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1 
                elif grid[r][c] == 2:
                    q.append((r, c))
        if not fresh:
            return 0 
        routing = 0
        minutes = -1
        direc = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while q:
            n = len(q)
            minutes += 1 
            for _ in range(n):
                row_, col_ = q.popleft() 

                for dr, dc in direc:
                    new_r = dr + row_
                    new_c = dc + col_ 
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        routing += 1
                        grid[new_r][new_c] = 2 
                        q.append((new_r, new_c))
        return minutes if fresh == routing else -1 

