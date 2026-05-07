class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0] * n 
        graph = defaultdict(list)
        for src, dst in relations:
            indegree[dst-1] += 1 
            graph[src-1].append(dst-1)  

        max_time = [0] * n
        
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                max_time[i] = time[i]  
        
        while q:
            node = q.popleft()
            
            for nei in graph[node]:
                max_time[nei] = max(max_time[nei], max_time[node] + time[nei])
                indegree[nei] -= 1
                
                if indegree[nei] == 0:
                    q.append(nei)
        
        return max(max_time)


"""class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0] * n 
        graph = defaultdict(list)
        for src, dst in relations:
            indegree[dst-1] += 1 
            graph[src].append(dst)

        q = deque([i+1 for i in range(n) if indegree[i]==0]) 
    
        total = 0 
        while q:
            level_size = len(q) 
            max_ = 0
            for _ in range(level_size):
                node = q.popleft()
                max_ = max(max_, time[node-1])
                for nei in graph[node]:
                    indegree[nei-1] -= 1 
                    if indegree[nei-1] == 0:
                        q.append(nei)
            total += max_ 
        return total """
