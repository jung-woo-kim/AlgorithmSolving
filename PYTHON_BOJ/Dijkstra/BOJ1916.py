import heapq
import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

bus = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    bus[a].append((c,b))


start,end = map(int,sys.stdin.readline().rstrip().split())


dp = [1e9 for _ in range(N+1)]

def Dijkstra(start):
    hq = []
    heapq.heappush(hq,(0,start))

    dp[start] = 0

    while hq:
        w,n = heapq.heappop(hq)

        #왜 있어야 하는거지..
        #아래에서 다 걸리는거 아닌가...?
        if dp[n] < w:
            continue

        for next_weight,next in bus[n]:
            if dp[next] > w+next_weight:
                dp[next] = w+next_weight
                heapq.heappush(hq,(w+next_weight,next))

Dijkstra(start)

print(dp[end])