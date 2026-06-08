from collections import Counter 
from heapq import heapify, heappop, heappush 

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        max_heap = []

        for letter, fre in freq.items():
            heappush(max_heap, (-fre, letter))
        
        order = []
        while max_heap:
            neg_fre, letter = heappop(max_heap)
            fre = -neg_fre 
            
            if order and order[-1] == letter:
                if max_heap: 
                    neg_sec, sec_letter = heappop(max_heap)
                    sec = -neg_sec  
                    
                    order.append(sec_letter)
                    if sec - 1 > 0:
                        heappush(max_heap, (-(sec - 1), sec_letter))
                    
                    heappush(max_heap, (-fre, letter)) 
                else:
                    return ""  
            else:
                order.append(letter)
                if fre - 1 > 0:
                    heappush(max_heap, (-(fre - 1), letter))  
        
        return "".join(order)



""" first trial 

from collections import Counter 
from heapq import heapify, heappop, heappush 
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        max_heap = []

        for letter, fre in freq.items():
            heappush(max_heap, (-fre, letter))
        
        order = []
        while max_heap:
            fre, letter = heappop(max_heap)
            fre = -fre 
            if order and order[-1] == letter:
                # this will be pushed back after getting the second most frequently appeared letter
                if max_heap: 
                    sec, sec_letter = heappop(max_heap)
                    sec = -sec
                    order.append(sec_letter)
                    if sec - 1 != 0:
                        heappush(max_heap, (-sec+1, sec_letter))

                    # then pushing back 
                    heappush(max_heap, (fre, letter))
                else:
                    #cannt go further, 
                    order = []
                    break 
            else:
                # add to the order and push back with 1 less frequency 
                order.append(letter)
                if fre - 1 != 0:
                    heappush(max_heap, (-fre + 1, letter)) 
        return "".join(order) if order else ""

"""


        