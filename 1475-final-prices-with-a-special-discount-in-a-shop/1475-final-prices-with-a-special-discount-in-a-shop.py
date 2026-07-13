class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        # required to find the first smallest or equal to an element 
        # build increasing stack 

        stack = []
        answer = [price for price in prices]

        for p in range(len(prices)):
            price = prices[p]
            while stack and prices[stack[-1]] >= price:
                ind = stack.pop()
                answer[ind] = answer[ind] - price 
            stack.append(p)
        return answer 
