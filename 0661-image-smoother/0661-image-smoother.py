class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row_len = len(img)
        col_len = len(img[0])
        
        new = [[0]* col_len for row in range(row_len)]

        for row in range(row_len):
            for col in range(col_len):
                count = 0
                summ = 0
                
                for r in range(max(0, row-1),min(row_len, row+2)):
                    for c in range(max(0, col-1), min(col_len, col+2)):
                        count += 1
                        summ += img[r][c]
                new[row][col] = summ//count

        return new        