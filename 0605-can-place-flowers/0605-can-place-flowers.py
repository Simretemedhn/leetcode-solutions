from math import floor, ceil

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not flowerbed:
            return n == 0
            
        count = 0
        total = 0
        i = 0
        length = len(flowerbed)
        
        while i < length and flowerbed[i] == 0:
            count += 1
            i += 1
        
        if i == length:
            total += ceil(count / 2)
            return total >= n
        
        total += floor(count / 2)
        count = 0
        
        for j in range(i, length):
            if flowerbed[j] == 0:
                count += 1
            else:
                if count > 0:
                    total += floor((count - 1) / 2)
                    count = 0
        
        if count > 0:
            total += floor(count / 2)
        
        return total >= n

        