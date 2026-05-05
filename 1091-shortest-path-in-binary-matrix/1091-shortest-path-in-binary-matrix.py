class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        target = len(grid) - 1
        
        if grid[0][0] == 1 or grid[target][target] == 1:
            return -1
            
        q = deque()
        q.append((0, 0, 1))  
        visited = set()
        visited.add((0, 0))
        
        direction = [(-1,0), (0,-1), (1,0), (0,1), (1,1), (1,-1), (-1,-1), (-1,1)]
        
        while q:
            n = len(q)
            for _ in range(n):
                row, col, length = q.popleft()
                if row == target and col == target:
                    return length
                    
                for dr, dc in direction:
                    new_r = row + dr
                    new_c = col + dc
                    if 0 <= new_r <= target and 0 <= new_c <= target:
                        if (new_r, new_c) not in visited and grid[new_r][new_c] == 0:
                            visited.add((new_r, new_c))
                            q.append((new_r, new_c, length + 1))
        return -1
