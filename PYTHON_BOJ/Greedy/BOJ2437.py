import heapq
import sys

N = int(sys.stdin.readline().rstrip())

li = list(map(int,sys.stdin.readline().rstrip().split()))

hq = [0]
check = False
for i in range(N):
    heapq.heappush(hq,li[i])
    if li[i] == 1:
        check = True
        
if not check:
    print(1)
    exit()

if len(hq) == 2:
    if hq[1] == 1:
        print(2)
    else:
        print(1)
    exit()

while len(hq)>1:
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    if len(hq) > 0:
        if a+b < hq[0]-1:
            print(a+b+1)
            exit()
        elif a+b >= hq[0]-1:
            heapq.heappush(hq,a+b)
    else:
        print(a+b+1)
        break

