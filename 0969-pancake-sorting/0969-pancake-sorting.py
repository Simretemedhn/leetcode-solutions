class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        
        def do_swapping(k):
            left = 0
            right = k - 1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        
        result = []
        
        for target in range(n, 0, -1):
            idx = arr.index(target)
            
            # If it's not already at the correct position
            if idx != target - 1:
                # If not at front, bring to front
                if idx != 0:
                    # FIXED: Use idx + 1, not idx - 1
                    do_swapping(idx + 1)
                    result.append(idx + 1)
                
                do_swapping(target)
                result.append(target)
        
        return result
                