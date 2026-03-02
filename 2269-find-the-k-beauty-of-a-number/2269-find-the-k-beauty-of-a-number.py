class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_s = str(num)
        count = 0

        for i in range(len(num_s)-k+1):
            curr = int(num_s[i:i+k])

            if curr != 0 and num % curr == 0:
                count += 1

        return 1 if len(num_s) == 1 else count




        