class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        def find_closest_heater(house: int) -> int:
            left, right = 0, len(heaters) - 1
            
            if house <= heaters[0]:
                return heaters[0] - house
            if house >= heaters[-1]:
                return house - heaters[-1]
            
            while left <= right:
                mid = (left + right) // 2
                if heaters[mid] == house:
                    return 0
                elif heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return min(house - heaters[right], heaters[left] - house)
        
        max_radius = 0
        for house in houses:
            max_radius = max(max_radius, find_closest_heater(house))
        
        return max_radius