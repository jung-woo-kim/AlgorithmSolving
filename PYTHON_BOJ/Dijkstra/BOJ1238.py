import heapq
import sys

N,M,X = map(int,sys.stdin.readline().rstrip().split())

edges = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,T = map(int,sys.stdin.readline().rstrip().split())
    edges[a].append((T,b))

dp = [sys.maxsize for _ in range(N+1)]

def Dijkstra(start):
    hq = []
    heapq.heappush(hq,(0,start))
    dp[start] = 0

    while hq:
        now_w,now_node = heapq.heappop(hq)

        if dp[now_node] < now_w:
            continue

        for next_w,next_node in edges[now_node]:
            if dp[next_node] > now_w + next_w:
                dp[next_node] = now_w + next_w
                heapq.heappush(hq,(now_w + next_w,next_node))


answer = 0

for i in range(1,N+1):
    temp = 0

    dp = [sys.maxsize for _ in range(N+1)]
    Dijkstra(i)
    temp += dp[X]

    dp = [sys.maxsize for _ in range(N+1)]
    Dijkstra(X)
    temp += dp[i]

    answer = max(answer,temp)

print(answer)