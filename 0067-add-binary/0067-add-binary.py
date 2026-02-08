class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a = "0" * (len(b)-len(a)) + a
        if len(b) < len(a):
            b = "0" * (len(a)-len(b)) + b

        result  = ""
        carry = 0
        for x in range(len(a)-1, -1, -1):
            sum = int(a[x]) + int(b[x]) + carry 
            if sum == 1:
                result = "1" + result 
                carry = 0

            elif sum == 2:
                result = "0" + result 
                carry = 1
            elif sum == 3:
                result = "1" + result 
                carry = 1 
            elif sum == 0:
                result = "0" +  result 
        if carry == 1:
            result = "1" + result 
        return result 