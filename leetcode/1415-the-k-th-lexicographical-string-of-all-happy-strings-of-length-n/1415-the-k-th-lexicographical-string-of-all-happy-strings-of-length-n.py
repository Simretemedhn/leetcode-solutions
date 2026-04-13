class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (1 << (n - 1)) 
        if k > total:
            return ""
        
        result = []
        k -= 1  
        
        group_size = total // 3
        letters = ['a', 'b', 'c']
        result.append(letters[k // group_size])
        k %= group_size
        
        for i in range(1, n):
            group_size //= 2
            prev = result[-1]
            if prev == 'a':
                choices = ['b', 'c']
            elif prev == 'b':
                choices = ['a', 'c']
            else: 
                choices = ['a', 'b']
        
            result.append(choices[k // group_size])
            k %= group_size
        
        return "".join(result)

