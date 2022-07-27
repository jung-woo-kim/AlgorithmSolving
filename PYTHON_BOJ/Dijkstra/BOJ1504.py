import heapq
import sys

N,E = map(int,sys.stdin.readline().rstrip().split())

INF = sys.maxsize
dp = [INF for _ in range(N+1)]
heap = []

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

v1,v2 = map(int,sys.stdin.readline().rstrip().split())

def Dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap,(0,start))

    while heap:
        w,now = heapq.heappop(heap)

        for weight,node in graph[now]:
            next_weight = w+weight
            if dp[node] > next_weight:
                dp[node] = next_weight
                heapq.heappush(heap,(next_weight,node))

##1-> v1 -> v2 -> N
Dijkstra(1)
temp1 = dp[v1]
dp = [INF for _ in range(N+1)]

Dijkstra(v1)
temp2 = dp[v2]
dp = [INF for _ in range(N+1)]

Dijkstra(v2)
temp3 = dp[N]
dp = [INF for _ in range(N+1)]

answer = temp1 + temp2 + temp3

##1-> v2 -> v1 -> N
Dijkstra(1)
temp1 = dp[v2]
dp = [INF for _ in range(N+1)]

Dijkstra(v2)
temp2 = dp[v1]
dp = [INF for _ in range(N+1)]

Dijkstra(v1)
temp3 = dp[N]

answer = min(answer,temp1 + temp2 + temp3)

print(answer if answer < sys.maxsize else -1)

