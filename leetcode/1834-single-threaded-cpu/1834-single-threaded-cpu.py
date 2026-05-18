from heapq import heappush, heappop

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        new = []
        for i in range(len(tasks)):
            start, process = tasks[i]
            new.append([start, process, i])
        
        new.sort(key=lambda x: x[0])
        
        current_time = new[0][0]  
        min_heap = []
        idx = 0  
        result = []
        
        while len(result) < len(tasks):
            while idx < len(new) and new[idx][0] <= current_time:
                heappush(min_heap, (new[idx][1], new[idx][2]))  
                idx += 1
            
            if not min_heap:
                current_time = new[idx][0]
                continue
            
            processing_time, original_index = heappop(min_heap)
            result.append(original_index)
            
            current_time += processing_time
        
        return result

""" first trial 
from heapq import heappush, heappop
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        new = []
        for i in range(len(tasks)):
            start, process = tasks[i]
            new.append([start, process, i]) 
        new.sort(key=lambda x: x[0])

        start = new[0][0]
        min_heap = []
        last_index_added = 0 
        for task in new:
            if task[0] == start:
                heappush(min_heap, (task[1], task[2])) 
                last_index_added = task[2] + 1 
        
        result = []
        while len(result) < len(tasks):
            #let allow cpu to work 
            processing_time, ind = heappop(min_heap)
            result.append(ind)  
            total_waiting_time =  start + processing_time
            for i in range(last_index_added, len(tasks)):
                if new[i][0] <= total_waiting_time:
                    heappush(min_heap, (task[1], task[2]))
                    last_index_added = task[2] + 1  
                else:
                    break 
        return result """