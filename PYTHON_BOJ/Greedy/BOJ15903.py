import heapq
import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
li = list(map(int,sys.stdin.readline().rstrip().split()))

hq = []

for num in li:
    heapq.heappush(hq,num)

for _ in range(m):
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    heapq.heappush(hq,a+b)
    heapq.heappush(hq,a+b)

print(sum(hq))
