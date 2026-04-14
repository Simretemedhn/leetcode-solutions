class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        if total//k == 0:
            return 0 
        low = 1
        high = total//k
        res = 0

        while low <= high:
            mid = (low + high)//2 
            count = 0 
            for candy in candies:
                count += candy//mid 
            if count >= k:
                res = mid 
                low = mid + 1 
            else:
                high = mid - 1 
        return res 
