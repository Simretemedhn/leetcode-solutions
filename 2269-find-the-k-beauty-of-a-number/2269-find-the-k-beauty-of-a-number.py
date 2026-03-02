class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_s = str(num)
        n = len(num_s)
        count = 0
        
        window_num = 0
        for i in range(k):
            window_num = window_num * 10 + int(num_s[i])
        

        if window_num != 0 and num % window_num == 0:
            count += 1
        
        power = 10 ** (k - 1)
        
        for i in range(k, n):
            left_digit = int(num_s[i - k])
            new_digit = int(num_s[i])
            
            window_num = (window_num - left_digit * power) * 10 + new_digit
            
            if window_num != 0 and num % window_num == 0:
                count += 1
        
        return count
    

