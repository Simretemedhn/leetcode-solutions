class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(num for num in nums if num % 2 == 0)
        result = []
        
        for val, idx in queries:
            old_value = nums[idx]
            new_value = old_value + val
            
            if old_value % 2 == 0: 
                even_sum -= old_value  
            
            if new_value % 2 == 0:  
                even_sum += new_value 
            
            nums[idx] = new_value
            result.append(even_sum)
        
        return result

