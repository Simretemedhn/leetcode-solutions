class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        cache = {}
        
        def pascal(row: int, col: int) -> int:
            if (row, col) in cache:
                return cache[(row, col)]
            
            if col == 0 or col == row:
                result = 1
            elif row <= 1:
                result = 1
            else:
                result = pascal(row - 1, col - 1) + pascal(row - 1, col)
            
            cache[(row, col)] = result
            return result
        
        result = []
        for i in range(rowIndex + 1):
            result.append(pascal(rowIndex, i))
        
        return result

"""first trial 
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        def rowI(row, col):
            if row <= 1:
                return 1 
            if col == 0 or col == row:
                return 1 
            else:
                return rowI(row - 1, col - 1) + rowI(row - 1, col)
        

        result = []
        for i in range(rowIndex + 1):
            num = rowI(rowIndex, i)
            result.append(num)
        
        return result """