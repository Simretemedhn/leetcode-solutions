class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        new_num = 0 
        given = x
        while x != 0:
            last_digit = x % 10 
            new_num = new_num * 10 + last_digit 
            x  //= 10 
        return given == new_num