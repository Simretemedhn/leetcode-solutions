class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1 
        
        result.append(newInterval)
        
        while i < n:
            result.append(intervals[i])
            i += 1
            
        return result



"""class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]: 
        new = []
        flag = False
        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][1]:
                lower_boundary = min(intervals[i][0], newInterval[0])
                for i in range(i, len(intervals)):
                    if newInterval[1] <= intervals[i][1]:
                        if newInterval[1] <= intervals[i][0]:
                            upper_boundary = newInterval[1]
                            new.append(intervals[i])
                        else:
                            upper_boundary = intervals[i][1]
                        flag = True
                        new.append([lower_boundary, upper_boundary])
                        continue
                    if flag:
                        new.append(intervals[i])
                break        
            else:
                new.append(intervals[i])               
        return new"""