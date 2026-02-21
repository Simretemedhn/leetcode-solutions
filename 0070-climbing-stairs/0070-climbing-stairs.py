class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2
        
        for step in range(3, n + 1):
            ways[step] = ways[step - 1] + ways[step - 2]
        
        return ways[n]
        