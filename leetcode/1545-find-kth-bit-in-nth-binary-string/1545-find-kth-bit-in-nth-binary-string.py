class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def flip_then_reverse(binaryy):
            res = []
            for bit in binaryy:
                flipped = int(bit)^1
                res.append(str(flipped))
            reverse = "".join(res)[::-1]
            return reverse


        def find(n):
            if n == 1:
                return "0"
            prev = find(n-1)
            return prev + "1" + flip_then_reverse(prev)
        
        return find(n)[k-1]
        