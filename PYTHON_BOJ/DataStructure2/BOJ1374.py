import sys
import heapq


N = int(sys.stdin.readline().rstrip())
lecture = []

for _ in range(N):
    Num,start,end = map(int,sys.stdin.readline().rstrip().split())
    lecture.append((start,end))

lecture.sort()

hq = []
heapq.heappush(hq,lecture[0][1])
answer = 1

for i in range(1,N):
    fast_end = heapq.heappop(hq)
    if lecture[i][0] >= fast_end:
        heapq.heappush(hq,lecture[i][1])
    else:
        heapq.heappush(hq,fast_end)
        heapq.heappush(hq,lecture[i][1])
    
    answer = max(len(hq),answer)

print(answer)