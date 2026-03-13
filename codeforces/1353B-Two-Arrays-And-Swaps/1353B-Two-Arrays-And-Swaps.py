t = int(input())

for _ in range(t):
  n, k = map(int, input().split())
  
  num_a = list(map(int, input().split()))
  num_b = list(map(int, input().split()))
  num_a.sort()
  num_b.sort(reverse = True)
  
  total = sum(num_a)
  for i in range(k):
    if num_b[i] > num_a[i]:
      total -= num_a[i]
      total += num_b[i]
  print(total)