class Solution:
    def reverseBits(self, n: int) -> int:
        def decimal_to_binary(n):
            if n == 0:
                return "0"
            if n == 1:
                return "1"
            return str(n % 2) + decimal_to_binary(n // 2)
        
        binary_lsb_first = decimal_to_binary(n)
        
        if len(binary_lsb_first) < 32:
            binary_lsb_first = binary_lsb_first + "0" * (32 - len(binary_lsb_first))
        
        binary_msb_first = binary_lsb_first[::-1]
        
        total = 0
        for i, bit in enumerate(binary_msb_first):
            if bit == "1":
                total += pow(2, i)
        return total
