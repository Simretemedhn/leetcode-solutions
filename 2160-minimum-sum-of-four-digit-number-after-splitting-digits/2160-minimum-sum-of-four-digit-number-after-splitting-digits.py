from heapq import heappop, heappush, heapify 

class Solution:
    def minimumSum(self, num: int) -> int:
        in_string = str(num)
        to_be_heaped = [int(i) for i in in_string]
        heapify(to_be_heaped) 
        
        pair_one = []
        pair_two = []
        
        for i in range(2):
            digit_for_pair_one = heappop(to_be_heaped)
            digit_for_pair_two = heappop(to_be_heaped)
            
            pair_one.append(digit_for_pair_one)
            pair_two.append(digit_for_pair_two)

        
        num1 = pair_one[0] * 10 + pair_one[1]
        num2 = pair_two[0] * 10 + pair_two[1]
        
        return num1 + num2