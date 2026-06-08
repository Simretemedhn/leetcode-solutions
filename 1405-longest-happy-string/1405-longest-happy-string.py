from heapq import heappush, heappop, heapify 

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a > 0:
            heappush(max_heap, (-a, "a"))
        if b > 0:
            heappush(max_heap, (-b, "b"))
        if c > 0:
            heappush(max_heap, (-c, "c"))
        
        order = []
        while max_heap:
            negative_freq, letter = heappop(max_heap)
            freq = -negative_freq 
            
            if len(order) >= 2 and order[-1] == letter and order[-2] == letter:
                if max_heap:
                    second_nega, sec_letter = heappop(max_heap)
                    second = -second_nega 
                    
                    order.append(sec_letter)
                    second -= 1
                    if second > 0:
                        heappush(max_heap, (-second, sec_letter))
                    
                    heappush(max_heap, (-freq, letter))
                else:
                    break
            else:
                if freq >= 2:
                    order.append(letter)
                    order.append(letter)
                    freq -= 2
                    if freq > 0:
                        heappush(max_heap, (-freq, letter))
                else:  
                    order.append(letter)
                    
        return "".join(order)
"""from heapq import heappush, heappop, heapify 

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a > 0:
            heappush(max_heap, (-a, "a"))
        if b > 0:
            heappush(max_heap, (-b, "b"))
        if c > 0:
            heappush(max_heap, (-c, "c"))
        
        order = []
        while max_heap:
            negative_freq, letter = heappop(max_heap)
            freq = -negative_freq 
            
            if order and order[-1] == letter:
                if max_heap:
                    second_nega, sec_letter = heappop(max_heap)
                    second = -second_nega 
                    
                    order.append(sec_letter)
                    second -= 1
                    if second > 0:
                        heappush(max_heap, (-second, sec_letter))
                    
                    heappush(max_heap, (-freq, letter))
                else:
                    return ""
            else:
                order.append(letter)
                freq -= 1
                if freq > 0:
                    heappush(max_heap, (-freq, letter))
                    
        return "".join(order)"""