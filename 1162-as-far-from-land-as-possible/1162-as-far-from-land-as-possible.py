class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])
        q = deque()
        answer = [[0]*col for _ in range(row)]
        visited = set()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    q.append((r, c, 0))
                    visited.add((r, c))
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:
            r, c, length = q.popleft()

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc 
                if 0 <= new_r < row and 0 <= new_c < col and (new_r, new_c) not in visited:
                    answer[new_r][new_c] = length + 1 
                    visited.add((new_r, new_c))
                    q.append((new_r, new_c, length + 1))

        max_val = 0 
        found = False 
        for r in range(row):
            for c in range(col):
                if answer[r][c] > max_val:
                    max_val = answer[r][c] 
                    found = True     
        return max_val if found else -1 