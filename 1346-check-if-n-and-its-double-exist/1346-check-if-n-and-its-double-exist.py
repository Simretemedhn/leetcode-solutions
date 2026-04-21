class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        n = len(arr)
        
        for i in range(n):
            low, high = i + 1, n - 1
            target = 2 * arr[i]
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
        
        for i in range(n):
            if arr[i] % 2 == 0:
                target = arr[i] // 2
                for j in range(n):
                    if j != i and arr[j] == target:
                        return True
        
        return False
        