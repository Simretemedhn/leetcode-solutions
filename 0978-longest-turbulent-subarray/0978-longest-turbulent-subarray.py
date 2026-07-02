class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def signn(prev, now):
            if prev < now:
                return "inc"
            elif prev > now:
                return "dec"
            else:
                return "None"
        
        sign = "None" 
        longest = 1
        n = len(arr)
        left = 0
        
        for right in range(1, n):
            current_sign = signn(arr[right-1], arr[right])
            
            if current_sign == sign and current_sign != "None":
                longest = max(longest, right - left)
                left = right - 1
            elif current_sign == "None":
                longest = max(longest, right - left)
                left = right
            sign = current_sign
        
        longest = max(longest, n - left)
        return longest
