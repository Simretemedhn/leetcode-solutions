class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque()
        q.append((entrance[0], entrance[1]))
        visited = set()
        visited.add((entrance[0], entrance[1]))  
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows = len(maze)
        cols = len(maze[0])
        level = 0 
        
        while q:
            n = len(q)
            level += 1 
            
            for _ in range(n):
                row, col = q.popleft()
                
                for dr, dc in direction:
                    new_r = row + dr
                    new_c = col + dc 
                    
                    if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited and maze[new_r][new_c] == ".":
                        if (new_r == 0 or new_r == rows - 1 or new_c == 0 or new_c == cols - 1):
                            return level
                        
                        visited.add((new_r, new_c))
                        q.append((new_r, new_c))
        return -1
