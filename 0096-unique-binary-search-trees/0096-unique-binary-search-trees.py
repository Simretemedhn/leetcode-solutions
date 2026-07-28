class Solution:
    def numTrees(self, n: int) -> int:
        # catalian formual 
        # (2n)! / ((n+1)! * n!) 

        def factorial(n):
            if n == 1:
                return 1 
            else:
                return n * factorial(n-1)
        return factorial(2 * n) // (factorial(n+1) * factorial(n))