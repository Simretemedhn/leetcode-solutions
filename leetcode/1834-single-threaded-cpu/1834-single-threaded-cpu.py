from heapq import heappush, heappop

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = [(enqueue, process, idx) for idx, (enqueue, process) in enumerate(tasks)]
        indexed_tasks.sort()
        
        result = []
        min_heap = []
        time = 0
        task_index = 0
        n = len(tasks)
        
        while task_index < n or min_heap:
            while task_index < n and indexed_tasks[task_index][0] <= time:
                enqueue, process, idx = indexed_tasks[task_index]
                heappush(min_heap, (process, idx))
                task_index += 1
            
            if not min_heap:
                time = indexed_tasks[task_index][0]
                continue
            
            process_time, idx = heappop(min_heap)
            result.append(idx)
            time += process_time
        
        return result