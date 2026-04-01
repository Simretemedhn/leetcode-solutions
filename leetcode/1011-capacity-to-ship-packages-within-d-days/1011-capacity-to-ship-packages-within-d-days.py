class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lowest = max(weights)
        highest = sum(weights)
        res = 0

        while lowest <= highest:
            mid = (lowest + highest)//2 

            count = 1
            part_sum = 0 
            for weight in weights:
                part_sum += weight
                if part_sum > mid:
                    count += 1 
                    part_sum = weight
            if count <=  days:
                highest = mid - 1 
                res = mid 
            elif count > days:
                lowest = mid + 1 
        return res 
                