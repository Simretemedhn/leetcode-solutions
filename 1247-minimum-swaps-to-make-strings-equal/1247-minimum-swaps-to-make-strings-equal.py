class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        total = s1 + s2
        if (total.count("x")%2 != 0) or (total.count("y")%2 != 0):
            return -1
        count_xy = 0
        count_yx = 0
        for i in range(len(s1)):
            if s1[i] + s2[i] == "xy":
                count_xy += 1
            elif s1[i] + s2[i] == "yx":
                count_yx += 1
            else:
                continue
        even_swaps = (count_xy // 2) + (count_yx // 2)
        left_part = 0
        if count_xy % 2:
            left_part += 2
        total = even_swaps + left_part
        return total
    
