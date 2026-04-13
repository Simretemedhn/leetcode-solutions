class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low_cap = max(weights)
        high_cap = sum(weights)
        res = 0
        
        while low_cap <= high_cap:
            mid_cap = (low_cap + high_cap) // 2 
            count = 1 
            cap = 0 
            
            for weight in weights:
                if cap + weight > mid_cap:
                    count += 1
                    cap = weight  
                else:
                    cap += weight
            
            if count <= days:
                res = mid_cap 
                high_cap = mid_cap - 1 
            else:  
                low_cap = mid_cap + 1 
        
        return res
                