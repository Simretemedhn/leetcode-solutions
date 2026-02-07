class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(x):
            if x>0:
                return int("1")
            elif x == 0:
                return int("0")
            else:
                return int("-1")
        product = 1
        for num in nums:
            product *= num 
        return signFunc(product)

        