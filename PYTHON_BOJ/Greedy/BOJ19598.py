import heapq
import sys

N = int(sys.stdin.readline().rstrip())

hq = []
meeting = []

for _ in range(0,N):
    S,T = map(int, sys.stdin.readline().rstrip().split())
    meeting.append((S,T))

meeting.sort()

heapq.heappush(hq,meeting[0][1])

for i in range(0,N):
    if meeting[i][1] < hq[0]:
        heapq.heappush(hq,meeting[i][1])
    else:
        heapq.heappop(hq)
        heapq.heappush(hq,meeting[i][1])

print(len(hq))


