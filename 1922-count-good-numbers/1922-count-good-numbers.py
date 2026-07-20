class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even_positions = (n + 1) // 2  # positions 0,2,4,...
        odd_positions = n // 2          # positions 1,3,5,...
        
        return (pow(5, even_positions, MOD) * pow(4, odd_positions, MOD)) % MOD