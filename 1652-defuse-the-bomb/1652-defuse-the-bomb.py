class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        
        if k == 0:
            return [0] * n
        
        result = [0] * n
        
        if k > 0:
            window_sum = 0
            for i in range(1, k + 1):
                window_sum += code[i % n]  
            result[0] = window_sum
            
            for i in range(1, n):
                window_sum = window_sum - code[i] + code[(i + k) % n]
                result[i] = window_sum
                
        else:  
            k = abs(k)
            window_sum = 0
            for i in range(n - k, n):
                window_sum += code[i % n]
            
            result[0] = window_sum
            
            for i in range(1, n):
                window_sum = window_sum - code[(i - k - 1) % n] + code[i - 1]
                result[i] = window_sum
        
        return result