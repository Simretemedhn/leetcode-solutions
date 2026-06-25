class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        all_row = len(img)
        all_col = len(img[0])
        new = [[0]* all_col for _ in range(all_row)]

        for row in range(all_row):
            for col in range(all_col):
                count = 0 
                sum_ = 0 
                for r in range(row-1, row +2, 1):
                    if r >= 0 and r < all_row:
                        for c in range(col-1, col+2, 1):
                            if c >=0 and c < all_col:
                                count += 1 
                                sum_ += img[r][c]
                avg = sum_ // count 
                new[row][col] = avg
        return new 
        
