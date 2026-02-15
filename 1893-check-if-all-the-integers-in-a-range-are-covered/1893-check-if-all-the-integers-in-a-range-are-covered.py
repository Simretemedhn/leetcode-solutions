class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for x in range(left, right+1):
            flag = False

            for y in ranges:
                if y[0] <= x and x<=y[1]:
                    flag = True 
                    break

            if flag == False:
                return False 
        return True 