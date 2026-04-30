class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row = len(isWater)
        col = len(isWater[0])
        q = deque()
        answer = [[0]*col for _ in range(row)]
        visited = set()

        for r in range(row):
            for c in range(col):
                if isWater[r][c] == 1:
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
        return answer 