class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # xxyy xy
        # yyxx yx

        # xy -> 2
        # yx -> 2
        # 1 + 1 = 2

        # xy -> 1
        # yx -> 1
        # ans -> 2

        # ans -> 4
        # 

        # xxyyxyxy x y
        # yyxxyxyx y x

        # xy -> 4 
        # yx -> 4
        # ans -> 2 + 2 = 4

        # xy -> 1
        # yx -> 1
        # ans -> 2
        # total -> 6
        # 
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
        # count_xy = 2
        # count_yx = 2
        # 2 -> 1 
        #  2 // 2 -> 1

        # count_xy = 5
        # count_yx = 5
        # 5 -> 2
        # 5 // 2 -> 2
        even_swaps = (count_xy // 2) + (count_yx // 2)
        left_part = 0
        if count_xy % 2:
            left_part += 2
        total = even_swaps + left_part
        return total
            #xy 3
            #yx 3
