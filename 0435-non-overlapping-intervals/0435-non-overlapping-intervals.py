class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x:x[1])

        count = 0 
        prev_start = float("-inf")
        for start, end in intervals:
            if start >= prev_start:
                count += 1 
                prev_start  = end 
        return len(intervals) - count
