class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        def bucket_sort(arr):
            if len(arr) < 2:
                return arr

            bucket_num = int(len(arr) ** 0.5) 
            buckets = [[] for _ in range(bucket_num)]
            min_val, max_val = min(arr), max(arr)  
            
            if min_val == max_val:
                return arr
            
            for num in arr:
                if num == max_val:
                    ind = bucket_num - 1
                else:
                    ind = (num - min_val) * bucket_num // (max_val - min_val)  
                buckets[ind].append(num)
            
            sorted_one = []
            for bucket in buckets:
                if bucket:
                    bucket.sort()  
                    sorted_one.extend(bucket)
            return sorted_one

        sorted_ = bucket_sort(nums)
        maximum = 0
        for i in range(1, len(sorted_)):
            maximum = max(maximum, sorted_[i] - sorted_[i-1])
        
        return maximum 
       
    