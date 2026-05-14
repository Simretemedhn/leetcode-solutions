from heapq import heappush, heappop, heapify

n = int(input())

commands = []
for _ in range(n):
    parts = input().split()
    if parts[0] == "removeMin":
        commands.append(("removeMin", None))
    else:
        commands.append((parts[0], int(parts[1])))  

heap = []
output = []

for cmd, val in commands:
    if cmd == "insert":
        heappush(heap, val)
        output.append(("insert", val))
    
    elif cmd == "removeMin":
        if not heap:
            dummy = 0  
            heappush(heap, dummy)
            output.append(("insert", dummy))
        heappop(heap)
        output.append(("removeMin", None))
    
    else:  
        while heap and heap[0] < val:
            heappop(heap)
            output.append(("removeMin", None))
        
        if not heap or heap[0] > val:
            heappush(heap, val)
            output.append(("insert", val))
        
        output.append(("getMin", val))

print(len(output))
for cmd, val in output:
    if cmd == "removeMin":
        print("removeMin")
    else:
        print(cmd, val)