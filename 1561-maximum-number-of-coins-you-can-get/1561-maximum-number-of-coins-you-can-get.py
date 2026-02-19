class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        x = -2
        accumu = 0
        for i in range(len(piles)//3):
            accumu += piles[x] 
            x -=2
        return accumu


        