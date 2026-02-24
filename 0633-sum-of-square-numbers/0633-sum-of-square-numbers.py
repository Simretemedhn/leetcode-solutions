class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = math.isqrt(c)
        while left <= right:
            result = pow(left, 2) + pow(right, 2)
            if result == c:
                return True 
            elif result < c:
                left += 1
            else:
                right -= 1
        return False 
            
        