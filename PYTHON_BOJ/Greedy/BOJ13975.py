import heapq
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    result = 0
    K = int(sys.stdin.readline().rstrip())
    file = list(map(int,sys.stdin.readline().rstrip().split()))
    hq = []
    for f in file:
        heapq.heappush(hq,f)
    
    while True:
        if len(hq) > 1:
            a = heapq.heappop(hq)
            b = heapq.heappop(hq)
            heapq.heappush(hq,a+b)
            result = result + a + b
        else:
            break
    
    print(result)