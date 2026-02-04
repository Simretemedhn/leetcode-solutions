class Solution:
    def sumOfMultiples(self, n: int) -> int:
        count = 0
        for x in range(1, n+1):
            if (x%3 == 0) or (x%5 == 0) or (x%7 ==0):
                count += x
        return count 

        