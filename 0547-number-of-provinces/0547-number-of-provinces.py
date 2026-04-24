class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)

        n = len(isConnected)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    graph[i+1].append(j+1)
                    graph[j+1].append(i+1)
        
        visited = set()
        def dfs(node):
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
                     
        count = 0
        for i in range(1, n+1):
            if i not in visited:
                dfs(i)
                count += 1 
        return count 
