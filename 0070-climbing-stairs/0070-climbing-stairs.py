class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        
        def climb(n):
            if n <= 2:
                return n
            elif n in cache:
                return cache[n]
            else:
                answer = climb(n-1) + climb(n-2)
                cache[n] = answer 
                return answer 
        return climb(n)