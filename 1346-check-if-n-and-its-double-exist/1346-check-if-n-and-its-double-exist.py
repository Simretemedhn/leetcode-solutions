class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        target = set(arr)
        for num in arr:
            if num == 0 and arr.count(0) >= 2:
                return True
            elif num != 0 and num * 2 in target:
                return True 
        return False 
