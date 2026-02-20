class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        n = len(arr)
        
        for target in range(n, 0, -1):
            ind = arr.index(target)
            
            if ind != target - 1:
                if ind != 0:
                    result.append(ind + 1)
                    arr[:ind+1] = arr[:ind+1][::-1]
                
                result.append(target)
                arr[:target] = arr[:target][::-1]
        
        return result
        


"""
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        new = sorted(arr)

        n = len(arr)
        placed = n
        output = []
        for i in range(n-1, -1, -1):
            ind = arr.index(new[i])
            if ind != i:
                output.append(ind+1)
                arr[:ind+1] = arr[:ind+1][::-1]
                output.append(placed-1)
                arr[:placed+1] = arr[:ind+1][::-1]
                placed -= 1
            else:
                placed -= 1
        return output
"""