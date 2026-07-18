class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def power(x):

            if 4 ** x > n:
                return False 
            elif 4 ** x == n:
                return True 
            else:
                return power(x+1)

        return power(0)
