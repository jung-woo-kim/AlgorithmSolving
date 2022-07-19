import sys
import heapq

N = int(sys.stdin.readline().rstrip())

max_hq = [] #오름
min_hq = [] #내림

mid = -1e9
answer = []
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num <= mid:
        heapq.heappush(max_hq,(-num,num))
    else:
        heapq.heappush(min_hq,num)
    
    if len(min_hq) > len(max_hq):
        temp = heapq.heappop(min_hq)
        heapq.heappush(max_hq,(-temp,temp))

    if len(min_hq) + 1 < len(max_hq):
        temp = heapq.heappop(max_hq)
        heapq.heappush(min_hq,temp[1])
    answer.append(max_hq[0][1])

    # print(max_hq)
    # print(min_hq)

    mid = max_hq[0][1]

for a in answer:
    print(a)