class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        
        go_right = True
        go_down = False
        go_left = False
        go_up = False
        
        output = []
        
        while top <= bottom and left <= right:
            if go_right:
                for col in range(left, right + 1):
                    output.append(matrix[top][col])
                top += 1
                go_right = False
                go_down = True
                
            elif go_down:
                for row in range(top, bottom + 1):
                    output.append(matrix[row][right])
                right -= 1
                go_down = False
                go_left = True
                
            elif go_left:
                if top <= bottom:
                    for col in range(right, left - 1, -1):
                        output.append(matrix[bottom][col])
                    bottom -= 1
                go_left = False
                go_up = True
                
            elif go_up:
                if left <= right:
                    for row in range(bottom, top - 1, -1):
                        output.append(matrix[row][left])
                    left += 1
                go_up = False
                go_right = True
        
        return output