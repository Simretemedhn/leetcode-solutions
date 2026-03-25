class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        memo = {}
        
        def add(level, i):
            if i == 0 or i == level:
                return 1
            
            if (level, i) in memo:
                return memo[(level, i)]
            
            result = add(level - 1, i - 1) + add(level - 1, i)
            memo[(level, i)] = result
            return result
        
        res = []
        for i in range(rowIndex + 1):
            res.append(add(rowIndex, i))
        
        return res