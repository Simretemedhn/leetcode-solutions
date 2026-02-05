class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        left = 0
        right = 3
        sliding_window =arr[left:right]
        for c in range(len(arr)-2):
            if arr[c] %2 != 0:
                if arr[c+1]%2 != 0 and arr[c+2]%2 !=0:
                    return True
        return False 
        


        