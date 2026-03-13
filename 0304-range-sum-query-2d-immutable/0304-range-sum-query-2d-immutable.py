class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.prefix = [[0] * (col + 1) for _ in range(row +1)]
        for i in range(1, row+1):
            for j in range(1, col+1):
                self.prefix[i][j] = matrix[i-1][j-1] + self.prefix[i-1][j] + self.prefix[i][j-1] - self.prefix[i-1][j-1]
        print(self.prefix)
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        my_row1 = row1 + 1
        my_col1 = col1 + 1
        my_row2 = row2 + 1 
        my_col2 = col2 + 1 
        return self.prefix[my_row2][my_col2] - self.prefix[my_row1-1][my_col2] - self.prefix[my_row2][my_col1-1] + self.prefix[my_row1-1][my_col1-1]

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)