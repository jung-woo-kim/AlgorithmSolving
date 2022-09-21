import heapq
import sys

V,E = map(int,sys.stdin.readline().rstrip().split())
INF = sys.maxsize
dp = [INF for _ in range(V+1)]
heap = []

graph = [[]for _ in range(V+1)]

for _ in range(E):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append((c,b))

answer = INF

def Dijkstra(start):
    heapq.heappush(heap,(0,start))
    while heap:
        w,n = heapq.heappop(heap)
        for wei,next_node in graph[n]:
            if dp[next_node] > w+wei:
                dp[next_node] = w+wei
                heapq.heappush(heap,(w+wei,next_node))

for i in range(1,V+1):
    dp = [INF for _ in range(V+1)]
    Dijkstra(i)
    answer = min(answer,dp[i])

print(answer if answer < INF else -1)