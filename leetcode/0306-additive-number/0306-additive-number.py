class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtracking(a1, a2, arry):
            if not arry:
                return True
            
            if arry[0] == '0':
                if int(a1) + int(a2) == 0:
                    return backtracking(a2, "0", arry[1:])
                return False
            
            for i in range(1, len(arry) + 1):
                next_num = arry[:i]
                if int(a1) + int(a2) == int(next_num):
                    if backtracking(a2, next_num, arry[i:]):
                        return True
            return False
        
        def choseFirstTwo(i):
            if i >= len(num) - 2:  
                return False
            
            a1 = num[:i+1]
            if len(a1) > 1 and a1[0] == '0':
                return choseFirstTwo(i+1)
            
            for j in range(i+1, len(num) - 1):  
                a2 = num[i+1:j+1]
                if len(a2) > 1 and a2[0] == '0':
                    continue
                
                remaining = num[j+1:]
                if backtracking(a1, a2, remaining):
                    return True           
            return choseFirstTwo(i+1)       
        return choseFirstTwo(0)
"""
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        a1 = None 
        a2 = None 
        def backtracking(a1, a2, arry):
            if arry[0] != 0:
                for i in range(len(arry)):
                    if int(a1) + int(a2) = arry[:i+1]:
                        if backtracking(a2, arry[:i+1], arry[i+1:]):
                            return True 

        def choseFirstTwo(i):
            if i == len(nums) :
                return 

            a1 = nums[:i+1]
            for j in range(i+1, len(nums)):
                if nums[i+1] != 0:
                    a2 = nums[i+1:j+1]
                    if backtracking(a1, a2, nums[j+1:]):
                        return True 
                    
            choseFirstTwo(i+1)
        return choseFirstTwo(0)
"""