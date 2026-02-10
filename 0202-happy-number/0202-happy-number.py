class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        sum = n

        while sum != 1:
            if sum in seen:
                return False   
            seen.add(sum)

            new_n = str(sum)
            sum = 0
            for x in new_n:
                sum += int(x) ** 2

        return True
"""class Solution:
    def isHappy(self, n: int) -> bool:
        curr_sum = n
        while curr_sum != 1 and curr_sum != 4:
            new_n = str(curr_sum)
            curr_sum = 0 
            for x in new_n:
                curr_sum += int(x) ** 2
          
        return curr_sum == 1 """



        