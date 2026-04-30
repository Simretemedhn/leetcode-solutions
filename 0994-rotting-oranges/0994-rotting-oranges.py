class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0 
        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1 
        
        if not fresh:
            return 0 
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        routing = 0
        minutes = 0 

        while q:
            n = len(q)
            minutes += 1

            for i in range(n):
                r, c = q.popleft()

                for dr, dc in directions:
                    new_r = r + dr 
                    new_c = c + dc 
                
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2 
                        q.append((new_r, new_c))
                        routing += 1 
                        
        return minutes-1 if routing == fresh else -1  
                    

