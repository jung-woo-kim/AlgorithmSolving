import heapq
import sys

N = int(sys.stdin.readline().rstrip())

time = []
hq = []

for i in range(0,N):
    S,T = map(int,sys.stdin.readline().rstrip().split())
    time.append((S,T))

time.sort()

heapq.heappush(hq,time[0][1])

i = 0
room = 0

answer = 0

for i in range(1,N):
    if  time[i][0] < hq[0]:
        heapq.heappush(hq,time[i][1])

    else:
        heapq.heappop(hq)
        heapq.heappush(hq,time[i][1])
        
print(len(hq))