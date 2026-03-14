class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_count = l_count = segment = 0
        for char in s:
            if char == "R":
                r_count += 1
            else:
                l_count += 1
            if r_count == l_count:
                segment += 1
                r_count == 0
                l_count == 0 
        
        return segment 
        