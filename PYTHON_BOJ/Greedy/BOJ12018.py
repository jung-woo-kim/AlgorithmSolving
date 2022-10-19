
import sys

n,m = map(int,sys.stdin.readline().rstrip().split())

min_mile = []

for _ in range(n):
    P,L = map(int,sys.stdin.readline().rstrip().split())
    mile = list(map(int,sys.stdin.readline().rstrip().split()))
    mile.sort(reverse=True)
    if P >= L:
        min_mile.append(mile[L-1] + 1)
    else:
        min_mile.append(1)

min_mile.sort()
now = 0
answer = 0
for mile in min_mile:
    now+=mile
    if now > m:
        break
    answer+=1
    
print(answer)    
