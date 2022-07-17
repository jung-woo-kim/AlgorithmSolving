import heapq
import sys

N = int(sys.stdin.readline().rstrip())

li = []

for _ in range(N):
    heapq.heappush(li,int(sys.stdin.readline().rstrip()))
   
answer = 0

for _ in range(N):
    lop = len(li)
    answer = max(answer,lop*heapq.heappop(li))

print(answer)