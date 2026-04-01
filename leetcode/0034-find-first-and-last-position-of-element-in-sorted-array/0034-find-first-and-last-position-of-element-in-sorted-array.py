class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low =0
        high = len(nums) -1 
        res = []
        if len(nums) == 0:
            return [-1, -1]
        starting_left = 0
        ending_right = 0

        while low <= high:       
            mid = (low + high)//2 
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1 
            else:
                starting_left = low                                  
                ending_right = high
                break 
                   
        while starting_left <= mid:
            if nums[starting_left] == target:
                res.append(starting_left)
                break 
            starting_left += 1 
        while ending_right >= mid:
            if nums[ending_right] == target:
                res.append(ending_right)
                break  
            ending_right -= 1 
        if res:
            return res 
        return [-1, -1]
        
