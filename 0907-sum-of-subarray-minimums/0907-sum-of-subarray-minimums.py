class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
        # Next smaller element (right side)
        next_smaller = []
        nextt = [1] * n
        
        for i in range(n - 1, -1, -1):
            curr = arr[i]
            
            # Pop elements GREATER than curr (maintain increasing stack)
            while next_smaller and next_smaller[-1][0] >= curr: 
                next_smaller.pop()
            
            if next_smaller:
                nextt[i] = next_smaller[-1][1] - i
            else:
                nextt[i] = n - i
            
            next_smaller.append((arr[i], i))
        
        # Previous smaller element (left side)
        prev_smaller = []    
        prev = [1] * n
        
        for i in range(n):
            curr = arr[i]
            
            # Pop elements GREATER than curr (maintain increasing stack)
            while prev_smaller and prev_smaller[-1][0] > curr:  
                prev_smaller.pop()
            
            if prev_smaller:
                prev[i] = i - prev_smaller[-1][1]
            else:
                prev[i] = i + 1
            
            prev_smaller.append((arr[i], i))
        
        # Calculate sum 
        total = 0
        for i in range(n):
            total = (total + nextt[i] * prev[i] * arr[i]) % MOD
        
        return total


""" or class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
        # Previous smaller element (strictly smaller)
        prev = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # Next smaller or equal element
        next_smaller = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            next_smaller[i] = stack[-1] if stack else n
            stack.append(i)
        
        # Calculate total sum
        total = 0
        for i in range(n):
            left = i - prev[i]
            right = next_smaller[i] - i
            total = (total + arr[i] * left * right) % MOD
        
        return total"""