import sys

D, N = map(int,sys.stdin.readline().rstrip().split())

oven = list(map(int,sys.stdin.readline().rstrip().split()))

pizza = list(map(int,sys.stdin.readline().rstrip().split()))

for i in range(1,D):
    oven[i] = min(oven[i],oven[i-1])

cur = 0
for i in range(D-1, -1, -1):
    if pizza[cur] > oven[i]:
        continue
    
    cur += 1
    if cur >= N:
        print(i+1)
        sys.exit(0)
 

print(0)