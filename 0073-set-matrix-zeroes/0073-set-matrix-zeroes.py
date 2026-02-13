class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_removed = []
        col_removed = []
        row_len = len(matrix)
        col_len = len(matrix[0])
        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == 0:
                    row_removed.append(row)
                    col_removed.append(col)
        for x in range(len(row_removed)):
            r = row_removed[x]
            for col in range(col_len):
                matrix[r][col] = 0
        for y in range(len(col_removed)):
            c = col_removed[y]
            for row in range(row_len):
                matrix[row][c] = 0
        

        