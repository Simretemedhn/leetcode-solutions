class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            papers = n - mid
            
            if citations[mid] >= papers:
                res = papers
                right = mid - 1  
            else:
                left = mid + 1  
        
        return res   
        
"""
        if n == 1 and citations[0] > 0:
            return 1

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n
        
        while left < right:
            mid = (left + right + 1) // 2  # Upper mid to avoid infinite loop
            
            # Check if h=mid is possible
            # We need at least 'mid' papers with >= mid citations
            # That means citations[n-mid] >= mid
            if citations[n - mid] >= mid:
                left = mid  # Try larger h
            else:
                right = mid - 1  # Try smaller h
        
        return left

"""