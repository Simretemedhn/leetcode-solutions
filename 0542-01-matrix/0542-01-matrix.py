class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)               
        col = len(mat[0])
        q = deque()  
        answer = [[0]*col for _ in range(row)]
        visited = set()
        
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    q.append((r, c, 0))  
                    visited.add((r, c))      
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]


        while q:
            rows, cols, length = q.popleft()
            
            for dr, dc in direction:
                new_r, new_c = rows + dr, cols + dc
                
                if 0 <= new_r < row and 0 <= new_c < col:
                    if (new_r, new_c) not in visited:
                        answer[new_r][new_c] = length + 1  
                        visited.add((new_r, new_c))
                        q.append((new_r, new_c, length + 1))
        
        return answer



        