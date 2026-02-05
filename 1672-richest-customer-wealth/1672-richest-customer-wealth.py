class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total = 0
        for money in accounts:
            total = max(total, sum(money))
        return total 

        