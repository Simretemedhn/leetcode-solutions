from collections import defaultdict, deque
                                    
length = int(input())
words = []
for _ in range(length):
    word = input()
    words.append(word)              

adjacency_list = defaultdict(list)
indegree = {chr(i + ord('a')): 0 for i in range(26)}

possible = True

for i in range(length - 1):
    word1, word2 = words[i], words[i + 1]
    n, m = len(word1), len(word2)
    
    j = 0
    while j < n and j < m and word1[j] == word2[j]:
        j += 1
    
    if j == n and j == m:
        continue  
    elif j == m and j < n:
        print("Impossible")
        possible = False
        break
    elif j == n and j < m:
        continue
    else:
        u, v = word1[j], word2[j]
        if v not in adjacency_list[u]:
            adjacency_list[u].append(v)
            indegree[v] += 1

if possible:
    q = deque([ch for ch in indegree if indegree[ch] == 0])
    result = []
    
    while q:
        node = q.popleft()
        result.append(node)
        for neighbor in adjacency_list[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    
    if len(result) == 26:
        print(''.join(result))
    else:
        print("Impossible")