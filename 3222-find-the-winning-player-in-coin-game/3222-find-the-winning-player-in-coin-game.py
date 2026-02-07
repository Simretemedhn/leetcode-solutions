class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        turn = min(x, y//4)
        if turn %2 != 0:
            return 'Alice'
        else:
            return "Bob"
        