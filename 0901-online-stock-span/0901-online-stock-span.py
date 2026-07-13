class StockSpanner:

    def __init__(self):
        # decreasing stack 
        self.prices = []
        # stack 
        self.span = []

    def next(self, price: int) -> int:
        result = []
        count = 1 

        while self.prices and self.prices[-1] <= price:
            count += self.span.pop() 
            self.prices.pop()
        self.prices.append(price)
        self.span.append(count)

        return count 

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)