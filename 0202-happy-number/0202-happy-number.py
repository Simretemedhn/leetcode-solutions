class Solution:
    def isHappy(self, n: int) -> bool:
        
        def digit_square(num):
            sum_  = 0
            while num > 0:
                digit = num % 10 
                sum_ += digit * digit

                num //= 10 
            return sum_ 
        
        slow = digit_square(n) 
        fast = digit_square(digit_square(n))
        while fast != 1:
            slow = digit_square(slow)
            fast = digit_square(digit_square(fast))

            if slow == fast:
                return False 
        return True 
