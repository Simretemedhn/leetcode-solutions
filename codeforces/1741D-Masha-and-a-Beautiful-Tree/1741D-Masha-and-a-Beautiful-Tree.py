import math

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    checking_times = int(math.log2(n))  
    
    rnd = 1
    count = 0
    while rnd <= checking_times:
        nex = 2**(rnd-1)
        for i in range(0, n, 2**rnd):
            left = i
            mid = i + nex
            if nums[left] > nums[mid]:  
                nums[left:mid], nums[mid:mid+nex] = nums[mid:mid+nex], nums[left:mid]
                count += 1
        rnd += 1 
    
    found = False 
    for i in range(1, n):
        if nums[i] < nums[i-1]:
            print(-1)
            found = True 
            break 
    if not found:
        print(count)