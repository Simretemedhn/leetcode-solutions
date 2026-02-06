class Solution:
    def intToRoman(self, num: int) -> str:
        latin = ""     
    
        if num//1000 >0:
            latin += "M" * (num//1000)
            num = num - ((num//1000)*1000)

        if num // 100>0:
            if num // 100 == 4:
                latin += "CD"
            elif num // 100 == 9:
                latin += "CM"
            elif num // 100 <4:
                latin += "C" * (num//100)

            else:
                latin += "D"
                latin += "C" * ((num//100)-5)
            num = num - ((num//100)*100)

        if num // 10>0:
            if num // 10 == 4:
                latin += "XL"
            elif num // 10 == 9:
                latin += "XC"
            elif num // 10 <4:
                latin += "X" * (num//10)

            else:
                latin += "L"
                latin += "X" * ((num//10)-5)
            num = num - ((num//10)*10)

        if num >0:
            if num  == 4:
                latin += "IV"
            elif num  == 9:
                latin += "IX"
            elif num  <4:
                latin += "I" * (num)

            else:
                latin += "V"
                latin += "I" * (num-5)
        return latin 


 



        