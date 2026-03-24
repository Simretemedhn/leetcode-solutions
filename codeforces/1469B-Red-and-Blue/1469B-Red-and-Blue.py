t = int(input())

for _ in range(t):
    n = int(input())
    list1 = list(map(int, input().split()))
    m = int(input())
    list2 = list(map(int, input().split()))
    
    max_1 = 0
    current = 0
    for num in list1:
        current += num
        max_1 = max(max_1, current)
    
    max_2 = 0
    current = 0
    for num in list2:
        current += num
        max_2 = max(max_2, current)
    
    print(max_1 + max_2)