class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        _row = len(heights)
        _col = len(heights[0])
        
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        def inbound(row, col):
            return 0 <= row < _row and 0 <= col < _col
        
        pacific_reachable = [[False] * _col for _ in range(_row)]
        atlantic_reachable = [[False] * _col for _ in range(_row)]
        
        def dfs(row, col, reachable):
            reachable[row][col] = True
            
            for dr, dc in direction:
                new_row, new_col = row + dr, col + dc
                
                if (inbound(new_row, new_col) and 
                    not reachable[new_row][new_col] and 
                    heights[new_row][new_col] >= heights[row][col]):
                    dfs(new_row, new_col, reachable)
        
        for i in range(_row):
            dfs(i, 0, pacific_reachable)  
        for j in range(_col):
            dfs(0, j, pacific_reachable)  
        
        for i in range(_row):
            dfs(i, _col - 1, atlantic_reachable)
        for j in range(_col):
            dfs(_row - 1, j, atlantic_reachable)  
        
        result = []
        for i in range(_row):
            for j in range(_col):
                if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                    result.append([i, j])
        
        return result
# first trial 

"""class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def pacific(row, col):
            return row < 0 or col < 0
        def atlantic(row, col):
            return row = _row or col = _col

        def pacific_dfs(row, col):
            if (row, col) in possible:
                return True 
            elif (row, col) in notPossible:
                return False            
            for dr, dc in direction:
                new_row = row + dr
                new_col = col + dc 
                if inbound(new_row, new_col) and  heights[row][col] >= heights[new_row][new_col]:
                    pacific_dfs(new_row, new_col)
        def atlantic_dfs(row, col):
            pass


        for r in range(_row):
            for c in range(_col):

                visit = pacific_dfs(r, c) and atlantic_dfs(r, c)
                if visit:
                    res.append([r, c])
                    possible.add((r, c))
                else:
                    notPossible.add((r, c))

"""