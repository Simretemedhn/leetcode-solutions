class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        collec = [1, 2]
        for x in range(3, n+1):
            collec.append(collec[-2] + collec[-1])
            
        return collec[-1]
        
