class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_char = defaultdict(int) 

        for char in s:
            s_char[char] += 1


        sum_ = 0
        for char, freq in s_char.items():
            if freq%2 == 0:
                sum_ += freq 
            else:
                sum_ += freq-1
        if sum_ < len(s):
            sum_ += 1
        return sum_ 

        