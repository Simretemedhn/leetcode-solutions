from collections import defaultdict 
class Solution:
    def customSortString(self, order: str, s: str) -> str:

        order_map = defaultdict(lambda: -1)
        for ind, char in enumerate(order):
            order_map[char] = ind

        list1 = list(s)
        for i in range(len(s)-1):  
            flag= False
            for x in range(len(s)-1-i): 
                if order_map[list1[x]] == -1:
                    continue 
                elif order_map[list1[x]] > order_map[list1[x+1]]:
                    list1[x], list1[x+1] = list1[x+1], list1[x] 
                    flag = True 
            if not flag:
                break
        return "".join(list1)