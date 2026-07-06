class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n
        
        while num != 1:
            if num in seen:
                return False 
            seen.add(num)

            num_Str = str(num)
            num = 0 
            for every in num_Str:
                num += int(every) ** 2 

        return True 