from copy import deepcopy
import heapq
import sys

N = int(sys.stdin.readline().rstrip())

hq = []
answer = 0

for _ in range(0,N):
    heapq.heappush(hq,int(sys.stdin.readline().rstrip()))

if N == 1:
    answer = 0
else:
    for _ in range(0,N-1):
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        answer = answer + a + b
        heapq.heappush(hq,a+b)

print(answer)