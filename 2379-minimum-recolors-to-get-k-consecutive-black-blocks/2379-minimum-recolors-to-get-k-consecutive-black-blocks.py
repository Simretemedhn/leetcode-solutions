class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        count_w = 0
        min_ = k+1

        for i in range(k):
            if blocks[i] == "W":
                count_w += 1
        min_ = min(min_, count_w)
        
        left = 0 
        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                count_w += 1
            if blocks[left] == "W":
                count_w -= 1
            left += 1
            min_ = min(min_, count_w)
        
        return min_


            




        